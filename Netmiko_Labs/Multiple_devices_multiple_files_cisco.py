from netmiko import ConnectHandler
with open('devices.txt')as f:
       router = f.read().splitlines()
       print(router)

router_list = list()
for ip in router:
       devices = {
              'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
              'host': ip,
              'username': 'Bharat',
              'password': 'Nyk@@123#',
              'port': 22,             # optional, default 22
              #'secret': 'cisco',      # this is the enable password
              'verbose': True         # optional, default False
              }
       router_list.append(devices)

for device in router_list:
        # connecting to the device and returning an ssh connection object
       connection = ConnectHandler(**devices)
       print('Entering into the enable mode....')
       connection.enable()
       file = input(f'Enter a configuration file (use a valid path for {device["host"]}:')
       print(f'Running commands from file: {file} on device: {device["host"]}')
       output = connection.send_config_from_file(file)
       print(output)

        # closing the connection
       print(f'Closing connection to device: {devices["host"]}')
       connection.disconnect()

       print('#'*30)