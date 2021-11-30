# Create a Python script that connects to a Cisco Router using Telnet, 
# enters the enable mode, and then executes the show run command. 
# Save the output to a file.

import telnetlib
import time
import getpass


# connecting to the remote device (telnet server)
tn = telnetlib.Telnet('192.168.122.101')

tn.read_until(b'Username: ')
tn.write(b'Bharat\n')  # sending the username

password = getpass.getpass('Enter your password: ')
tn.read_until(b'Password: ')
tn.write(f'{password}\n'.encode())  # sending the user's password

tn.write(b'terminal length 0\n')
tn.write(b'show run\n')
tn.write(b'exit\n')
time.sleep(1)

# getting and printing the output
output = tn.read_all()
output = output.decode()
print(output)

