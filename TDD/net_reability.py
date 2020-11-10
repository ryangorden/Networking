import os
from yaml import safe_load

with open('hosts.yml', 'r') as file:
    hosts= safe_load(file)

for host in hosts['Hosts']:
    os.system('ping -c 1 ' + host)
