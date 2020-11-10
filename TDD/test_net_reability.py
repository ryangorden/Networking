import os
import pytest
from yaml import safe_load
import sys

def test_good_get_hosts(file='hosts.yml'):
    '''
    validate that the file is a yml file a value is  a list
    '''

    if 'yml' or 'yaml'not in file:
        sys.exit('hosts file in not yaml file or file does not exist')
    with open(file, 'r') as new_file:
        hosts= safe_load(new_file)

    assert isinstance(hosts,dict)



def test_bad_get_hosts(file='hosts.txt'):
    '''
    validate that the file is a yml file a value is  a list
    '''

    if 'yml' not in file:
        sys.exit('hosts file need to be in a yaml file')
    elif 'yaml' not in file:
        sys.exit('hosts file need to be in a yaml file')
    with open(file, 'r') as new_file:
        hosts= safe_load(new_file)

    assert isinstance(hosts,dict)
