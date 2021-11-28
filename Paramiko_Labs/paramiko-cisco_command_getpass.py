import paramiko
import time
import getpass

# creating an ssh client object
ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
#                    look_for_keys=False, allow_agent=False)

password = getpass.getpass('Enter the password:')
router = {'hostname': '192.168.122.100', 'port': '22', 'username':'Bharat', 'password':password}
print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)  # using **kwargs

#Establishing the shell with network devices
shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('show ip interface brief\n') 
time.sleep(1)

output = shell.recv(10000)

print(type(output))
#decoding the byte typr file to normal text file

output = output.decode('utf-8')
print(output)

# checking if the connection is active and closing the active connection

if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()