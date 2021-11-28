from netmiko import ConnectHandler

cisco_device = { 
    'device_type': 'cisco_ios',
    'ip': '192.168.122.101',
    'username':'Bharat',
    'password':'Nyk@@123#',
    'port':'22',
    'secret':'Nyk@@123#',
    'verbose':True

    }

net_connect = ConnectHandler(**cisco_device)
prompter = net_connect.find_prompt()
if '>' in prompter: 
    net_connect.enable()

interface = input('Please enter the interface: ')
output = net_connect.send_command('show ip interface ' + interface)

if 'Invalid input detected' in output:
    print('You have entered invalid interface')

else: 
    first_line = output.splitlines()[0]
    print(first_line)

if not 'up' in first_line:
    print('The interface is down. Enabling the interface...')
    commands = ['interface ' + interface, 'no sh', 'exit']
    output = net_connect.send_config_set(commands)
    print(output)
    print('#' * 40)
    print(interface + ' Interface has been enabled')
else:
    print('The' + interface + ' interface was already enabled')


net_connect.disconnect()
