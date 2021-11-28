import paramiko
import time
# import getpass

# creating an ssh client object
ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.122.105', port='22', username='osboxes', password='osboxes.org',
                   look_for_keys=False, allow_agent=False)
# password = getpass.getpass('Enter your password here:')
# router1 = {'hostname': '192.168.122.101', 'port': '22', 'username':'Bharat', 'password': password}
# router2 = {'hostname': '192.168.122.102', 'port': '22', 'username':'Bharat', 'password': password}
# router3 = {'hostname': '192.168.122.103', 'port': '22', 'username':'Bharat', 'password': password}

# routers = [router1, router2, router3]


print(f'Connecting to 192.168.122.105')
# ssh_client.connect(**router, look_for_keys=False, allow_agent=False)  # using **kwargs

shell = ssh_client.invoke_shell()
shell.send('ip addr\n')
shell.send('cat /etc/passwd\n')
shell.send('osboxes.org\n')
time.sleep(1)
shell.send('cat /etc/shadow\n')
shell.send('osboxes.org\n')
time.sleep(1)
output = shell.recv(1000).decode()
print(output)


# checking if the connection is active and closing the active connection

if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()