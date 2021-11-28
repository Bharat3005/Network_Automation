import telnetlib
import time
import getpass

router1 = {'host': '192.168.122.101', 'user': 'Bharat', }
router2 = {'host': '192.168.122.102', 'user': 'Bharat', }
router3 = {'host': '192.168.122.103', 'user': 'Bharat', }


routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router["host"]}')
    password = getpass.getpass('Enter your password: ')

    tn = telnetlib.Telnet(host=router['host'])

    tn.read_until(b'Username: ')
    tn.write(router['user'].encode() + b'\n')

    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')

    tn.write(b'terminal length 0\n')
    tn.write(b'enable\n')
    tn.write(password.encode() + b'\n')  # this is the enable password

    tn.write(b'conf t\n')
    tn.write(b'ip route 0.0.0.0 0.0.0.0 192.168.122.1\n')
    tn.write(b'end\n')
    tn.write(b'show ip route\n')
    tn.write(b'exit\n')
    time.sleep(1)

    output = tn.read_all()
    output = output.decode()
    print(output)
    print('#' * 50)