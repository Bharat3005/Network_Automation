import time
class Devices:
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
        print(f'Sending commands: {command}')
        self.tn.write(command.encode() + b'\n')
        time.sleep(timeout)
    
    # def show(self):
    #     output = self.tn.read_all().decode('utf-8')
    #     return output

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output

router1 = Devices(host= '192.168.122.101', username= 'Bharat', password='Nyk@@123#')
router1.connect()
router1.authenticate()
router1.send('enable')
router1.send('config t')
router1.send('int lo0')
router1.send('ip add 1.1.1.1 255.255.255.255')
router1.send('exit')
router1.send('router ospf 100')
router1.send('network 0.0.0.0 0.0.0.0 area 0')
router1.send('end')
router1.send('terminal length 0')
router1.send('show ip protocols')
router1.send('show ip int br')
# router1.send('show run')

output = router1.show()
print(output)