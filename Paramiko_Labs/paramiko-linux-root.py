import paramiko
import time

# creating an ssh client object
ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
linux = {'hostname': '192.168.122.105', 'port': '22', 'username': 'osboxes', 'password': 'osboxes.org'}                
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

print(f'connecting to {linux ["hostname"]}') #=> Printing on the screen
 
#Actual command send to the server 
stdin, stdout, stderr = ssh_client.exec_command('sudo useradd pragati\n', get_pty=True)
stdin.write('osboxes.org\n')
time.sleep(5)
stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
time.sleep(5)
output = stdout.read().decode()
print(output)



# checking if the connection is active and closing the active connection

if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()