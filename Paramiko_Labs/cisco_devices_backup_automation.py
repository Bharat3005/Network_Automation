from datetime import datetime
import myparamiko
router1 = {'server_ip': '192.168.122.101', 'server_port': '22', 'user': 'Bharat', 'passwd': 'Nyk@@123#'}
client = myparamiko.connect(**router1)
shell = myparamiko.get_shell(client)

myparamiko.send_command(shell, 'terminal length 0')
myparamiko.send_command(shell, 'enable')
myparamiko.send_command(shell, 'show run')

output = myparamiko.show(shell)

#print(output)
output_list = output.splitlines()
output_list = output_list[11:-1]

#printing the output as list 
output = '\n'.join(output_list)

#printing the output
print(output)

#Backup file saving according to date amd time
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

file_name = f'{router1["server_ip"]}_{year}-{month}-{day}-{hour}-{minute}.txt'
print(file_name)

#saving the output to the file
# with open('router1_backup.txt', 'w') as f:# => This is very generic way to do the backup with routers name it is not recommended above procedure is recommeded.
#     f.write(output)
# myparamiko.close(client)


with open(file_name, 'w') as f:
    f.write(output)
myparamiko.close(client)