import napalm
import json
from napalm import get_network_driver
driver = get_network_driver('ios')

optional_args = {'secret': 'Nyk@@123#'} ###This is a secret password
ios = driver('192.168.122.244', 'Bharat', 'Nyk@@123#', optional_args=optional_args)
ios.open()

ios.load_replace_candidate(filename='RW1_config.txt')
diff = ios.compare_config()
#print(diff)

if len(diff):
    print(diff)
    print('commit changes....')
    ios.commit_config()
    print('Done')

else: 
    print('No changes required....')
ios.discard_config()


ios.close() 