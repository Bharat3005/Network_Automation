from netmiko import Netmiko
connection = Netmiko(host= '192.168.122.100', port= '22', username= 'Bharat', password='Cisco@123', device_type= 'cisco_ios')

from netmiko import ConnectHandler
import netmiko

cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '192.168.122.100',
       'username': 'Bharat',
       'password': 'Cisco@123',
       'port': 22,             # optional, default 22
       #'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }

connection = netmiko.ConnectHandler(**cisco_device)

output = connection.send_command('show ip int br')

print(output)

connection.disconnect()
