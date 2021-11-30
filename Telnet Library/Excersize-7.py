# Create a Python script that connects to a Cisco Router using Telnet and 
# executes a list of commands. The commands are saved in a Python list.
# An example of a list with commands to execute:
# the second element (cisco) is the enable command
# commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 
# 'access-list 1 permit any', 'end', 'terminal length 0', 'sh run | i user']


import telnetlib
import time

# connecting to the remote device (telnet server)
tn = telnetlib.Telnet('192.168.122.101')

tn.read_until(b'Username: ')
tn.write(b'Bharat\n')  # sending the username

tn.read_until(b'Password: ')
tn.write(b'Nyk@@123#\n')  # sending the user's password

# the second element (cisco) is the enable command
commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end',
            'terminal length 0',  'sh run | i user']
for cmd in commands:
    tn.write(cmd.encode() + b'\n')


tn.write(b'exit\n')
time.sleep(2)

# getting and printing the output
output = tn.read_all().decode()
print(output)
