import json
import sys
import requests
from jinja2 import Environment, FileSystemLoader
from requests.auth import HTTPBasicAuth
from yaml import safe_load

sys.path.append('/mnt/c/Users/ryan.gorden/Downloads/Git_files/Networking/restconf')
from creds import my_creds

server= "https://10.10.20.100/"

resource="restconf/data/ietf-interfaces:interfaces/"

url= f"{server}{resource}"

headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

auth= HTTPBasicAuth(my_creds["username"], my_creds["password"])




# I am opening my data file
with open('vars/var_interface.yml') as file:
    interfaces = safe_load(file)

# This is combining my data file with the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/template_interface.j2')
payload = template.render(data=interfaces)

requests.packages.urllib3.disable_warnings()
resp= requests.post(url, headers=headers, auth=auth, data= payload, verify=False)

# raise flags for any errors which may happen along the way
resp.raise_for_status()

if resp.status_code == 201:
    print(resp.status_code)
    resource2="restconf/data/ietf-interfaces:interfaces/interface=Loopback500"
    url= f"{server}{resource2}"
    resp2= requests.get(url, headers=headers, auth=auth, verify=False)
    print(resp2.text)
    #resp2 = requests.delete(url, headers=headers, auth=auth, verify=False)
