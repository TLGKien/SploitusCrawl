import msgpack
import http.client
from decouple import config


class Msfrpc:
  class MsfError(Exception):
    def __init__(self,msg):
      self.msg = msg
    def __str__(self):
      return repr(self.msg)

  class MsfAuthError(MsfError):
    def __init__(self,msg):
      self.msg = msg
    
  def __init__(self,opts=[]):    
    """
    Initialize an instance of the Msfrpc client.

    Args:
        opts (dict, optional): A dictionary of options to configure the client.
            Supported options:
            - 'host' (str): The host where the Metasploit RPC service is running.
            - 'port' (int): The port to connect to the RPC service.
            - 'uri' (str): The URI path for the RPC service.
            - 'ssl' (bool): Whether to use SSL for the connection. Default is False.

    Attributes:
        host (str): The host where the Metasploit RPC service is running.
        port (int): The port to connect to the RPC service.
        uri (str): The URI path for the RPC service.
        ssl (bool): Whether to use SSL for the connection.
        authenticated (bool): Indicates whether the client is authenticated.
        token: Authentication token.
        headers (dict): HTTP headers for the RPC request.
        client: An HTTP(S) connection object.

    Example:
        Initialize a client with custom options:
        ```
        custom_opts = {
            'host': 'metasploit-server',
            'port': 55553,
            'uri': '/api/v1',
            'ssl': True
        }
        client = Msfrpc(custom_opts)
        ```
    """
    self.host = opts.get('host') or config('SERVER_HOST')
    self.port = opts.get('port') or config('SERVER_PORT')
    self.uri = opts.get('uri') or config('SERVER_URI')
    self.ssl = opts.get('ssl') or False
    self.authenticated = False
    self.token = False
    self.headers = {"Content-type" : "binary/message-pack" }
    if self.ssl:
      self.client = http.client.HTTPSConnection(self.host,self.port)
    else:
      self.client = http.client.HTTPConnection(self.host,self.port)
 
  def encode(self,data):
    return msgpack.packb(data)
  def decode(self,data):
    return msgpack.unpackb(data)

  def call(self,meth,opts = []):
    """
    Call a method on the Metasploit RPC service.

    Args:
        meth (str): The name of the method to call.
        opts (list, optional): A list of options to pass to the method. Default is an empty list.

    Returns:
        dict: A dictionary containing the response from the RPC service.

    Raises:
        MsfAuthError: If the method requires authentication and the client is not authenticated.

    Example:
        To call a method named 'module.info' with some options:
        ```
        client = Msfrpc()
        if client.login('your_username', 'your_password'):
            response = client.call('module.info', ['exploit/multi/http/php_cgi_arg_injection'])
            print(response)
        else:
            print("Authentication failed.")
        ```
    """
    if meth != "auth.login":
      if not self.authenticated:
        raise self.MsfAuthError("MsfRPC: Not Authenticated")

    if meth != "auth.login":
      opts.insert(0,self.token)

    opts.insert(0,meth)
    params = self.encode(opts)
    self.client.request("POST",self.uri,params,self.headers)
    resp = self.client.getresponse()
    return self.decode(resp.read()) 
  
  def login(self,user,password):
    """
    Authenticate with the Metasploit RPC service using a username and password.

    Args:
        user (str): The username for authentication.
        password (str): The password for authentication.

    Returns:
        bool: True if authentication is successful, False otherwise.

    Raises:
        MsfAuthError: If authentication fails.

    Example:
        To authenticate with the Metasploit RPC service:
        ```
        client = Msfrpc()
        if client.login('your_username', 'your_password'):
            print("Authentication successful.")
        else:
            print("Authentication failed.")
        ```
    """
    ret = self.call('auth.login',[user,password])
    if ret.get(b'result') == b'success':
      self.authenticated = True
      self.token = ret.get(b'token')
      return True
    else:
      raise self.MsfAuthError("MsfRPC: Authentication failed")


