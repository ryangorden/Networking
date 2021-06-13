from yaml import safe_load
from yaml import safe_load
from jinja2 import Environment, FileSystemLoader

def test_good_get_file():
    '''
    validate that file is dictionary with a list as the key
    '''

    with open(file="vars/var_DHCP.yml") as new_file:
        vars= safe_load(new_file)

    assert isinstance(vars,dict)
    assert isinstance(vars['dhcp'],list)

def tes_template_payload(template_name,vars):
    env= Environment(loader=FileSystemLoader("."))
    template= env.get_template(template_name)
    payload= template.render(vars)

    return payload
