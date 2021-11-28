import paramiko
import time
import getpass

# creating an ssh client object
ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
#                    look_for_keys=False, allow_agent=False)
password = getpass.getpass('Enter your password here:')
router1 = {'hostname': '192.168.122.101', 'port': '22', 'username':'Bharat', 'password': password}
router2 = {'hostname': '192.168.122.102', 'port': '22', 'username':'Bharat', 'password': password}
router3 = {'hostname': '192.168.122.103', 'port': '22', 'username':'Bharat', 'password': password}

routers = [router1, router2, router3]

for router in routers:

    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)  # using **kwargs

    shell = ssh_client.invoke_shell()
    shell.send('enable\n')
    shell.send('configure t\n')
    shell.send('router ospf 100\n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('wr\n')
    shell.send('show ip protocols\n')
    time.sleep(3)

    output = shell.recv(1000).decode()
    print(output)


# checking if the connection is active and closing the active connection

if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()