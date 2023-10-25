import sys
import logging
from pymsfrpc.msfrpc import Msfrpc
from decouple import config

class AutoExploit(Msfrpc):
  def search_modules(self, opts):
    """
    Search for Metasploit modules by name.

    Args:
      opts (list of str): A list containing the name of the module(s) to search for.

    Returns:
      list: A list of modules that match the provided module name(s).

    Example:
      To search for modules with names containing 'exploit/multi/http':
      matching_modules = self.search_modules(['exploit/multi/http'])
    """
    modules = self.call("module.search", opts)
    # Display modules
    for module in modules:
      print(module)
    return modules

  def show_options(self, opts):
    """
    Show the options for a Metasploit module.

    Args:
        opts (list): A list containing the name of the module. The ModuleName must include module type prefix ("exploit/") or similar.

    Returns:
        dict: A dictionary containing the module's options.

    Example:
        To show the options for a module named 'exploit/multi/http/php_cgi_arg_injection':
        options = self.show_options(['exploit/multi/http/php_cgi_arg_injection'])
    """

    # convert opts to [Module_type, Module_name]
    opts = opts[0].split('/', 1)
    print(opts)

    module_options = self.call("module.options", opts)

    # check if response is error?
    if module_options.get('error') == True:
      logging.error(f"Error code {module_options.get('error_code')}")
      logging.error(f"Error message: {module_options.get('error_message').decode('utf-8')}")
      sys.exit(1)

    # Display options of module
    for option, attributes in module_options.items():
      # option name decode
      if isinstance(option, bytes):
        option = option.decode('utf-8')
      print(f"OPTION: {option}")

      # attribute of option
      for attribute, attribute_value in attributes.items():
        # field decode
        if isinstance(attribute, bytes):
          attribute = attribute.decode('utf-8')
        # field value decode
        if isinstance(attribute_value, bytes):
          attribute_value = attribute_value.decode('utf-8')
        print(f"{attribute}: {attribute_value}")
      print('-' * 40)

    return module_options

  def runTest(self):
    # arguments is required
    if len(sys.argv) < 2:
      logging.error("Tham so bat buoc")
      sys.exit(1)

    # Get arguments
    meth = sys.argv[1]
    opts = sys.argv[2:]

    # Call method
    if meth == "module.search":
      modules = self.search_modules(opts)
      print('=' * 40)
      module_info = self.show_options([modules[0].get(b'fullname')])
    elif meth == "module.options":
      module_info = self.show_options(opts)

if __name__ == "__main__":
  auto_exploit = AutoExploit({})
  auto_exploit.login(config('USERNAME'), config('PASSWORD'))
  auto_exploit.runTest()