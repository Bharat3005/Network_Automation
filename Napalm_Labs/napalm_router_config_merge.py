from typing import Optional
from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'Nyk@@123#'}
ios = driver('192.168.122.244', 'Bharat', 'Nyk@@123#', optional_args=optional_args)
ios.open()

ios.load_merge_candidate('acl.txt')
diff = ios.compare_config()
#print(diff)

if len (diff) > 0:
    print(diff)
    answer = input('Commit Changes yes|no')
    if answer == 'yes':
        print('commiting the changes on the device')
        ios.commit_config()
    else:
        print('No changes required on the device')
        ios.discard_config()

ios.close()