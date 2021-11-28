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
stdin, stdout, stderr = ssh_client.exec_command('who\n') #=> stdin,stdout,sterr are the commands for input/output/error
time.sleep(5) #=> wait for 5 sec to capture the output
output = stdout.read() #=> reading binary based output
output = output.decode() #=> decding the binary based output to text based output
print(output)

stdin, stdout, stderr = ssh_client.exec_command('sudo ifconfig\n')
# stdin, stdout, stderr = ssh_client.exec_command('osboxes.org\n')
time.sleep(5)
output = stdout.read()
output = output.decode()
print(output)
print(stderr.read().decode()) #=> printing the input/output/error

# checking if the connection is active and closing the active connection

if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()