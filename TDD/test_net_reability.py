from yaml import safe_load


def test_good_get_hosts(file='reachable_hosts.yml'):
    '''
    validate that the file is a yml file a value is  a list
    '''
    with open(file, 'r') as new_file:
        hosts= safe_load(new_file)

    assert isinstance(hosts,dict)
    assert isinstance(hosts['Hosts'],list)



def test_bad_get_hosts(file='invalid_hosts.txt'):
    '''
    validate that only yaml file is passed in.
    '''

    if 'yml' not in file:
        assert 'yml' not in file



def test_good_ping_host(host_list= ['8.8.8.8','yahoo.com']):
    '''
    validate that a list of host was passed through
    '''

    assert isinstance(host_list,list) == True




def test_bad_ping_host(host_list= {}):
    '''
    validate that a list of host was passed through
    '''

    assert isinstance(host_list,list) == False
