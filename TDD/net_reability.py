import json
import subprocess
import sys
from yaml import safe_load



def get_host(file='reachable_hosts.yml'):
    '''
    function input looking yaml file with hosts.
    will return the host in a python list.
    '''

    if 'yml' not in file:
        sys.exit('Invalid filename: Check to see if file exist or verify it is a yaml file')
    else:
        with open(file, 'r') as new_file:
            hosts= safe_load(new_file)
    return hosts['Hosts']


def ping_hosts(hosts_list):
    '''
    This function takes a list of host and  check to see
    if they are reachable.
    '''
    output_list =[]
    for host in hosts_list:

        output=subprocess.check_output(['ping', '-c', '1 ', host])
        output_list.append(output)
    return json.dumps(output_list)

if __name__ == '__main__':
    hosts_list= get_host()
    is_reachable = ping_hosts(hosts_list)
    print(is_reachable)
