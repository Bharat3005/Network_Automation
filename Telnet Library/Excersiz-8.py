# Create a Python script that connects to a Cisco Router using Telnet 
# and executes all the commands from a text file.
# An example of a text file with commands.


import telnetlib
import time

# connecting to the remote device (telnet server)
tn = telnetlib.Telnet('192.168.122.101')

tn.read_until(b'Username: ')
tn.write(b'Bharat\n')  # sending the username

tn.read_until(b'Password: ')
tn.write(b'Nyk@@123#\n')  # sending the user's password

with open('command.txt', 'r') as f:
    commands = f.read().splitlines()
    print(commands)

for cmd in commands:
    print('Sending commands to device...')
    tn.write(cmd.encode() + b'\n')
    time.sleep(1)

tn.write(b'exit\n')
time.sleep(2)

# getting and printing the output
output = tn.read_all().decode()
print(output)