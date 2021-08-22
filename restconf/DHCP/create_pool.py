import requests
from jinja2 import Environment, FileSystemLoader
from yaml import safe_load
from requests.auth import HTTPBasicAuth


def get_file(file):
    '''
    validate that file is dictionary with a list as the key
    '''

    with open(file) as new_file:
        value= safe_load(new_file)

    return value

def template_payload(template_name,values):
    env= Environment(loader=FileSystemLoader("."))
    template= env.get_template(template_name)
    payload= template.render(info=values)

    return payload


server= "https://10.10.20.48/"
resource="restconf/data/Cisco-IOS-XE-native:native/ip/dhcp/"
url= f"{server}{resource}"


headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

auth= HTTPBasicAuth("developer", "C1sco12345")

values = get_file("vars/var_dhcp_rest.yml")
template_name= "templates/template_dhcp.j2"
resp_data= template_payload(template_name, values)

# Replace single quote with double quotes to make
# data json compliant
new_data=resp_data.replace("'",'"')



requests.packages.urllib3.disable_warnings()
resp= requests.post(url, headers=headers, auth=auth, data= new_data, verify=False)
requests.packages.urllib3.disable_warnings()

if resp.status_code == 201:
    print("DHCP Scope Create")
else:
    print("Failed")
