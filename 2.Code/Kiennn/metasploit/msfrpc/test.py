
from pymsfrpc.msfrpc import Msfrpc
from decouple import config


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