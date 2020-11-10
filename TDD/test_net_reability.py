import os
import pytest
from yaml import safe_load
import sys

def test_good_get_hosts(file='hosts.yml'):
    '''
    validate that the file is a yml file a value is  a list
    '''
    with open(file, 'r') as new_file:
        hosts= safe_load(new_file)

    assert isinstance(hosts,dict)



def test_bad_get_hosts(file='hosts.txt'):
    '''
    validate that the file is a yml file a value is  a list
    '''

    if 'yml' or 'yaml' not in file:
        sys.exit('Invalid file: hosts file not in yaml or does not exist')
    with open(file, 'r') as new_file:
        hosts= safe_load(new_file)

    assert isinstance(hosts,dict)
