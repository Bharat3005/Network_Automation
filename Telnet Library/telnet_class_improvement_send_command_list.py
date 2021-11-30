import time

class Device:
    def __init__(self, host, username, password, tn=None):
        self.host = host
        self.username = username
        self.password = password
        self.tn = tn

    def connect(self):
        import telnetlib
        self.tn = telnetlib.Telnet(self.host)

    def authenticate(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.username.encode() + b'\n')

        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')

    def send(self, command, timeout=0.5):
        print(f'Sending command: {command}')
        self.tn.write(command.encode() + b'\n')
        time.sleep(timeout)

#This is the send_from_list class added in the script for sending commands from the list
    def send_form_list(self, commands):
        for cmd in commands:
            self.send(cmd) #using self.send method for sending commands

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output




router = Device(host='192.168.122.101', username='Bharat', password='Nyk@@123#')
router.connect()
router.authenticate()
commands = ['enable', 'conf t', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit',
            'router ospf 1', 'net 0.0.0.0 0.0.0.0 area 0', 'end', 'term len 0', 'show ip protocols', 'exit']


router.send_form_list(commands)
output = router.show()
print(output)

