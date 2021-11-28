from typing import Optional
from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'Nyk@@123#'}
ios = driver('192.168.122.244', 'Bharat', 'Nyk@@123#', optional_args=optional_args)
ios.open()

answer = input('Do you want to rollback the config yes|no')
if answer == 'yes':
    print('Rolling back the configuration')
    ios.rollback()
    print('Done')

ios.close()

