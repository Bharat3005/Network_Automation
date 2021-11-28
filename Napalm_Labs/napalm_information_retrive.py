from typing import Optional
from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'Nyk@@123#'}
ios = driver('192.168.122.101', 'Bharat', 'Nyk@@123#', optional_args=optional_args)
ios.open()

# output = ios.get_facts()
# dump = json.dumps(output, sort_keys=True, indent=4)
# print(dump)

# output1 = ios.get_interfaces()
# dump =json.dumps(output1, sort_keys=True, indent=4)
# print(dump)

output = ios.get
dump =json.dumps(output, sort_keys=True, indent=4)
print(dump)

ios.close()


