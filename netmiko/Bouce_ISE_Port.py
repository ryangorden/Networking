from __future__ import print_function , absolute_import
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# retrieval of login information
try:
    username = raw_input('Enter your Username (AD credentials): ')
    password = getpass()
    enable = raw_input('Eneter your enable password: ')
except (NameError):
    username = input('Enter your Username (AD credentials): ')
    password = getpass()
    enable = input('Eneter your enable password: ')

# variables of device location
SIS_1stfloor = '10.120.1.201'
SIS_2ndfloor = '10.120.1.202'
SYS0_midlle_hall = '10.120.1.31'
SYS0_main_floor = '10.120.1.22'

# show the user list ip address to select form
nac_devices = [SIS_1stfloor, SIS_2ndfloor, SYS0_midlle_hall, SYS0_main_floor]
print('\n SIS_1stfloor          SIS_2ndfloor          SYS0_midlle_hall          SYS0_main_floor')
print(' {2:21} {0:21} {1:25} {3:10}'.format(nac_devices[2], nac_devices[0], nac_devices[1], nac_devices[3]))
try:
    ip_address = raw_input('Enter IP Address from list above of the device you want to connect to: ')
except (NameError):
    ip_address = input('Enter IP Address from list above of the device you want to connect to: ')

# retrieve the full mac address of the laptop/desktop
try:
    mac_address = raw_input('Enter your mac address int H.H.H format: ')
except (NameError):
    mac_address = input('Enter your mac address int H.H.H format: ')


# Information on what the system will use to connect to the device
network_device = {'device_type': 'cisco_ios',
                  'ip': ip_address,
		  'username': username,
		  'password': password,
		  'secret': enable
		 }

# Establish an ssh session to the network device
net_connect = ConnectHandler(**network_device)

# Enter privledge mode on the device
output_enable = net_connect.enable()



# This part of the program is looking for mac type which will be STATIC is controled by ISE
output_show = net_connect.send_command('show mac address-table address ' + mac_address)
mac_counter_static = 0 # this being used to count 
mac_counter_static = output_show.find('STATIC')

# this if statement will only be true if the Type for the mac entered is static
if mac_counter_static > 0:
    mac_lines = output_show.split()[13:]
    mac_lines_to_dict = {'vlan': mac_lines[0], 'type': mac_lines[2],
                         'interface': mac_lines[3], 'mac': mac_lines[1]
                        }
    print('This mac was found on a ISE controlled port')
    print('It was found on interface ' + mac_lines_to_dict['interface'])
    config_commands = ['int ' + mac_lines_to_dict['interface'], 'shutdown', 'no shutdown']
    config = net_connect.send_config_set(config_commands)
    print('true')
else:
    print('false')
# when are now logging off of the device
log_off = net_connect.disconnect
    
