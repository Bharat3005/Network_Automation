# Create a Python script that connects to a Cisco Router using 
# Telnet and executes the show users command in order to display 
# the logged-in users.
#Print out the output of the command.

import telnetlib
import time

# connecting to the remote device (telnet server)
tn = telnetlib.Telnet('192.168.122.101')

tn.read_until(b'Username: ')
tn.write(b'Bharat\n')  # sending the username

tn.read_until(b'Password: ')
tn.write(b'Nyk@@123#\n')  # sending the user's password

tn.write(b'show users\n')
tn.write(b'exit\n')
time.sleep(1)

# getting and printing the output
output = tn.read_all()
output = output.decode()
print(output)
