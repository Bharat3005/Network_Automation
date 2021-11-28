from netmiko import ConnectHandler
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '192.168.122.100',
       'username': 'Bharat',
       'password': 'Cisco@123',
       'port': 22,             # optional, default 22
       #'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }

 # connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)
print('Entering into the enable mode....')
connection.enable()
output = connection.send_config_from_file('ospf.txt')
print(output)
print(connection.find_prompt())
connection.send_command('write memory')

 # closing the connection
print('Closing connection')
connection.disconnect()
