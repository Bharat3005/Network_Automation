# Change the solution from the previous challenge so that it will prompt the user 
# for its password without echoing (use getpass module). 
# Run the script in the terminal (you can not run it in PyCharm).

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

tn.write(b'show users\n')
tn.write(b'exit\n')
time.sleep(1)

# getting and printing the output
output = tn.read_all()
output = output.decode()
print(output)
