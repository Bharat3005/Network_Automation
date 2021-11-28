from netmiko import ConnectHandler
import datetime
import time
import threading #implements threading in Python

# getting the current time as a timestamp
start = time.time()

def backup(device):
    connection = ConnectHandler(**device)
    print('Entering the enable mode...')
    connection.enable()

    output = connection.send_command('show run')
    # print(output)

    # creating the backup filename (hostname_date_backup.txt)
    prompt = connection.find_prompt()
    hostname = prompt[0:-1] #=> Slicing of the prompt to get hostname without the # sign
    # print(hostname)

    # getting the current date (year-month-day)
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    # creating the backup filename (hostname_date_backup.txt)
    filename = f'{hostname}_{year}-{month}-{day}_backup.txt'

    # writing the backup to the file
    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} completed successfully')
        print('#' * 30)


    print('Closing connection')
    connection.disconnect()

with open('devices.txt') as f:
    devices = f.read().splitlines()

threads = list()

for ip in devices:

    device = {
           'device_type': 'cisco_ios',
           'host': ip,
           'username': 'Bharat',
           'password': 'Nyk@@123#',
           'port': 22,             # optional, default 22
           #'secret': 'cisco',      # this is the enable password
           'verbose': True         # optional, default False
           }

    #backup(device)

    th = threading.Thread(target=backup, args=(device,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

end = time.time()
print(f'Total time for a execution:{end-start}')