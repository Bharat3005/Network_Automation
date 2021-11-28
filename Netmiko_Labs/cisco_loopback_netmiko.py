from netmiko import ConnectHandler
# creating a dictionary for the device to connect to
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
print('Entering to the enable mode....')
connection.enable()

commands = ['int lo0', 'ip add 1.1.1.1 255.255.255.255', 'exit',
            'int lo1', 'ip add 1.1.2.1 255.255.255.255', 'exit']
output = connection.send_config_set(commands)
print(output)
print(connection.find_prompt())
connection.send_command('write memory')

# closing the connection
print('Closing connection')
connection.disconnect()
################################################################################

#Method : 2


from netmiko import ConnectHandler
 # creating a dictionary for the device to connect to
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
print('Entering to the enable mode....')
connection.enable()

cmd = 'int lo3;ip add 1.1.3.1 255.255.255.255;exit;int lo4;ip add 1.1.4.1 255.255.255.255;exit'
output = connection.send_config_set(cmd.split(';'))
print(output)
print(connection.find_prompt())
connection.send_command('write memory')

 # closing the connection
print('Closing connection')
connection.disconnect()

####################################################################
#Method: 3

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
print('Entering to the enable mode....')
connection.enable()

cmd = ''' int lo5 
ip add 1.1.5.1 255.255.255.255
exit
int lo6
ip add 1.1.6.1 255.255.255.255
exit
'''
output = connection.send_config_set(cmd.split('\n'))
print(output)
print(connection.find_prompt())
connection.send_command('write memory')

 # closing the connection
print('Closing connection')
connection.disconnect()
