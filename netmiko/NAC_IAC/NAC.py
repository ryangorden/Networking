from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
from yaml import safe_load
from identity import credz

# I am opening my data file
with open('access_port_vars.yml') as file:
    port = safe_load(file)


# This is a list that contain my host
host_file = ['10.120.1.202']

# This is the information needed to log into devices
device_profile = []
for fqdn in host_file:
    device= { 'username': credz['user'],
              'password': credz['pass'],
              'secret': credz['enable'],
              'device_type': 'cisco_ios',
              'ip': fqdn
              }
    device_profile.append(device)


# This is combining my data file with the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('no_nac_int_template .j2')
#template = env.get_template('nac_int_template.j2')
commands = template.render(data=port)
print(commands)

# This is my function that is logging into devices and configuring them
def send_config():
    for device in device_profile:
        print('Connecting to ' + device['ip'])
        conn = ConnectHandler(**device)
        print('Entering Enable mode')
        conn.enable()
        print('Sending commands to device')
        config= conn.send_config_set(commands)
        host = conn.find_prompt()[:-1]
        print('Writing output to a file')
        with open(host +'.txt', 'w') as file2:
            file2.write(config)



# This is the actual program
if __name__ == '__main__':
    send_config()
    
    
