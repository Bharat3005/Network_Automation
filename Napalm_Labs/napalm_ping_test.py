from typing import Optional
from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'Nyk@@123#'}
ios = driver('192.168.122.101', 'Bharat', 'Nyk@@123#', optional_args=optional_args)
ios.open()

#############Normal_Ping###########################
# output = ios.ping('1.1.1.1')
# ping = json.dumps(output, sort_keys=True, indent = 4)
# print(ping)

################Extended_Ping######################
output = ios.ping(destination='1.1.1.1', count=2, source='192.168.122.101')
ping = json.dumps(output, sort_keys=True, indent=4)
print(ping)

ios.close()