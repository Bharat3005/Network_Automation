import paramiko
import time
from scp import SCPClient

# Remote device connection
ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.122.105', port='22', username='osboxes', password='osboxes.org',
                   look_for_keys=False, allow_agent=False)

scp = SCPClient(ssh_client.get_transport())
#copy single file operation

#scp.put('192.168.122.101_2021-10-20-20-1.txt', '/tmp/R2.txt')

#copy directory to the remote system

scp.put('Cisco_config', recursive=True, remote_path='/tmp/')

#copy file from remote server to client
scp.get('/etc/passwd', 'passwd-1')

scp.close()