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
    self.host = opts.get('host') or config('HOST')
    self.port = opts.get('port') or config('PORT')
    self.uri = opts.get('uri') or config('URI')
    self.ssl = opts.get('ssl') or False
    print(self.ssl)
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
    ret = self.call('auth.login',[user,password])
    if ret.get(b'result') == b'success':
      self.authenticated = True
      self.token = ret.get(b'token')
      return True
    else:
      raise self.MsfAuthError("MsfRPC: Authentication failed")

if __name__ == '__main__':
  
  # Create a new instance of the Msfrpc client with the default options
  client = Msfrpc({})

  client.login(config('USERNAME'),config('PASSWORD'))

  # Get a list of the exploits from the server
  mod = client.call('module.exploits')
  print(mod.get(b"modules")[0])
  
  # Grab the first item from the modules value of the returned dict
  print ("Compatible payloads for : %s\n" % mod[b'modules'][0])
  
  # Get the list of compatible payloads for the first option
  ret = client.call('module.compatible_payloads',[mod[b'modules'][0]])
  for i in (ret.get(b'payloads')):
    print ("\t%s" % i)

