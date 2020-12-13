import requests
from requests.auth import HTTPBasicAuth
from creds import my_creds
from yaml import safe_load
from jinja2 import Environment, FileSystemLoader
import json

with open("route_var.yml", "r") as file:
    var= safe_load(file)

env= Environment(loader=FileSystemLoader("."))
template= env.get_template("route_template.j2")
payload= template.render(var)


auth= HTTPBasicAuth(my_creds['username'], my_creds['password'])

server="https://ios-xe-mgmt.cisco.com:9443"
global_routes= "/restconf/data/ietf-routing:routing/routing-instance=default"
static_route="/routing-protocols/routing-protocol=static,1/static-routes/ipv4"

url= f"{server}{global_routes}{static_route}"

headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'}

response = requests.post(url, headers=headers,auth=auth,data=payload, verify= False)

print(response.status_code)

