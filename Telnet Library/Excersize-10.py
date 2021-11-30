# Consider a topology with multiple devices like this one.
# For each device in the topology, you have a Python dictionary that stores the Telnet connection 
# information (IP, username, password) 
# but also a filename that contains the commands to be sent to that device.
# Example:
# r1 = {'host': '192.168.122.10', 'username': 'Bharat', 'password': 'cisco', 'config':'ospf.txt'}
# r2 = {'host': '192.168.122.20', 'username': 'Bharat', 'password': 'cisco', 'config':'eigrp.txt'}
# r3 = {'host': '192.168.122.30', 'username': 'Bharat', 'password': 'cisco', 'config':'router3.conf'}
# ….
# Create a Python script that connects to each device using Telnet and executes the commands from the file (which is the value of the dictionary config key).
# Use the Telnet Class that was developed in the course or create the entire Python script from scratch.


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

    def send_form_list(self, commands):
        for cmd in commands:
            self.send(cmd)

    # new method that sends all the commands from a file
    def send_from_file(self, file):
        with open(file, 'r') as f:
            commands = f.read().splitlines()
            # print(commands)
            for cmd in commands:
                self.send(cmd)

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output


r1 = {'host': '192.168.122.101', 'username': 'Bharat', 'password': 'Nyk@@123#', 'config':'ospf.txt'}
r2 = {'host': '192.168.122.102', 'username': 'Bharat', 'password': 'Nyk@@123#', 'config':'eigrp.txt'}
r3 = {'host': '192.168.122.103', 'username': 'Bharat', 'password': 'Nyk@@123#', 'config':'router3.conf'}

routers = [r1, r2, r3]
for r in routers:
    router = Device(host=r['host'], username=r['username'], password=r['password'])
    router.connect()
    router.authenticate()

    router.send_from_file(r['config'])
    output = router.show()
    print(output)
    print('#' * 50)