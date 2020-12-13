import requests
from requests.auth import HTTPBasicAuth
from creds import my_creds

auth= HTTPBasicAuth(my_creds['username'], my_creds['password'])

server="https://ios-xe-mgmt.cisco.com:9443"
global_routes= "/restconf/data/ietf-routing:routing/routing-instance=default"
static_route="/routing-protocols/routing-protocol=static,1/static-routes/ipv4/route=192.168.1.0%2F24"

url= f"{server}{global_routes}{static_route}"

headers = {
  'Accept': 'application/yang-data+json'}

response = requests.delete(url, headers=headers,auth=auth, verify= False)
print(response.status_code)

