
class devices:
    def __init__(self, host, username, password, tn=None):
        self.host = host
        self.username = username
        self.password = password
        self.tn = tn

    def connection(self):
        import telnetlib
        self.tn = telnetlib.Telnet(self.host)

    def authentication(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.username.encode() + b'\n')
        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')
    
    def send(self, command, timeout=0.5):
        print(f'Sending commands: {command}')
        self.tn.write(command.encode() + b'\n')
        self.time.sleep(timeout)
    
    def show(self):
        output = self.tn.read_all().decode('uff-8')
        return output