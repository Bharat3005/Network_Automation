import myparamiko
import getpass

#=> input function is used to capture the admin input
username = input('username:')
#=> getpass module to capture the root password
password = getpass.getpass()

ssh_client = myparamiko.connect('192.168.122.105', '22', username, password)
remote_connection = myparamiko.get_shell(ssh_client)
#=> new_user object is created to add new user
new_user = input('Enter the user want to created:')
#=> adding new user in /home and /bin/bash directory
command = 'sudo useradd -m -d /home/' + new_user + ' -s /bin/bash' + new_user
myparamiko.send_command(remote_connection, command)
myparamiko.send_command(remote_connection, password)
print('A new user has been created.')

answer = input('Display the new user? <y|n>')
if  answer == 'y': 
    users = myparamiko.send_command(remote_connection, 'cat /etc/passwd')
    print(users.decode())
    
myparamiko.close(ssh_client)