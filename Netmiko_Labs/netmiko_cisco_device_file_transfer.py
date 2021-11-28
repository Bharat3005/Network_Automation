from netmiko import ConnectHandler
from netmiko import file_transfer

cisco_device = { 
    'device_type': 'cisco_ios',
    'ip': '192.168.122.244',
    'username':'Bharat',
    'password':'Nyk@@123#',
    'port':'22',
    'secret':'Nyk@@123#',
    'verbose':True

    }

connection = ConnectHandler(**cisco_device)

transfer_output = file_transfer(connection,source_file='ospf.txt', dest_file='ospf-1.txt', file_system= 'disk0:', direction='put', overwrite_file=True)

print(transfer_output)

connection.disconnect()
