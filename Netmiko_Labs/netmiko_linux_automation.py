from netmiko import ConnectHandler
import time

linux = {
           'device_type': 'linux',
           'host':'192.168.122.105',
           'username':'osboxes',
           'password':'osboxes.org',
           'port': 22,             # optional, default 22
           'secret': 'osboxes.org',      # this is the enable password
           'verbose': True         # optional, default False
           }

connection = ConnectHandler(**linux)
connection.enable()

output = connection.send_command('apt update && apt install -y htop')
time.sleep(10)
print(output)

print('closing the connection')
connection.disconnect()
