from netmiko import ConnectHandler
from getpass import getpass

# retrieval of login information
try:
    username = raw_input('Enter your Username (AD credentials): ')
    password = getpass()
    enable = raw_input('Eneter your enable password: ')
except (NameError):
    username = input('Enter your Username (AD credentials): ')
    password = getpass()
    enable = input('Eneter your enable password: ')


# enter ip of device you want to connect to or use dns name
try:
    ip_address = raw_input('Enter IP Address  or DNS name of the device you want to connect to: ')
except (NameError):
    ip_address = input('Enter IP Address or DNS name of the device you want to connect to: ')


# enter port number
try:
    port= raw_input('Enter the port to ssh to the device on (default is 22): ') or 22
except (NameError):
    port= input('Enter the port to ssh to the device on (default is 22): ') or 22



# Information on what the system will use to connect to the device
network_device = {'device_type': 'cisco_ios',
                  'ip': ip_address,
                  'username': username,
                  'password': password,
                  'secret': enable,
                  'port': port
                 }


# Establish an ssh session to the network device
net_connect = ConnectHandler(**network_device)

# Enter privledge mode on the device
if '>' in net_connect.find_prompt():
    output_enable = net_connect.enable()
else:
    print('Already in enable mode')


# This part of the program is looking for mac type which will be STATIC is controled by ISE
acl_webauth_redirect = net_connect.send_config_from_file('acl_webauth_redirect.txt')
print(acl_webauth_redirect)

# when are now logging off of the device
net_connect.disconnect
