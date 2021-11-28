from datetime import datetime
import myparamiko
import threading

#=> Lets create a function called as Backup 

def backup(router):
    client = myparamiko.connect(**router)
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
    #print(output)

    #Backup file saving according to date amd time
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    file_name = f'{router["server_ip"]}_{year}-{month}-{day}-{hour}-{minute}.txt'
    print(file_name)

    #saving the output to the file
    # with open('router1_backup.txt', 'w') as f:# => This is very generic way to do the backup with routers name it is not recommended above procedure is recommeded.
    #     f.write(output)
    # myparamiko.close(client)


    with open(file_name, 'w') as f:
        f.write(output)
    myparamiko.close(client)

router1 = {'server_ip': '192.168.122.101', 'server_port': '22', 'user': 'Bharat', 'passwd': 'Nyk@@123#'}
router2 = {'server_ip': '192.168.122.102', 'server_port': '22', 'user': 'Bharat', 'passwd': 'Nyk@@123#'}
router3 = {'server_ip': '192.168.122.103', 'server_port': '22', 'user': 'Bharat', 'passwd': 'Nyk@@123#'}

routers = [router1, router2, router3]
threads = list() #=> creating list for multithreading 

for router in routers: #=> applying for loop for a Multithreading
    th = threading.Thread(target=backup, args=(router, )) #=> creating th variable with target and args.
    threads.append(th) #=> appeinding  the th variable in threads list

for th in threads: #=> for loop to start the treading with th.start() function
    th.start()

for th in threads: #=> for loop to join the treading with th.join() function to join the output
    th.join()   

    