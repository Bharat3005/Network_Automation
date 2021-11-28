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
prompt = connection.find_prompt()
print(prompt)
if '>' in prompt:
    connection.enable()

prompt = connection.find_prompt()
print(prompt)

# sending a command and getting the output
output = connection.send_command('sh run')
print(output)
print(connection.check_config_mode())
if not connection.check_config_mode():
    connection.config_mode()

print(connection.check_config_mode())
connection.send_command('username Pragati secret 9 Nyk@@123#')
connection.exit_config_mode()
print(connection.check_config_mode())



# closing the connection
print('Closing connection')
connection.disconnect()