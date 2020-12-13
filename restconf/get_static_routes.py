import requests
from requests.auth import HTTPBasicAuth
from creds import my_creds

auth= HTTPBasicAuth(my_creds['username'], my_creds['password'])

server="https://ios-xe-mgmt.cisco.com:9443"
global_routes= "/restconf/data/ietf-routing:routing/routing-instance=default"
static_route="/routing-protocols/routing-protocol=static,1/static-routes/"

url= f"{server}{global_routes}{static_route}"

headers = {
  'Accept': 'application/yang-data+json'}

response = requests.get(url, headers=headers,auth=auth, verify= False).json()

print("\nDestination    Next-Hop")
print("\n-------------- --------------------")

data= response['ietf-routing:static-routes']['ietf-ipv4-unicast-routing:ipv4']['route']

for routes in data:
    try:
        print("\n{:14} {:20}".format(routes['destination-prefix'], routes['next-hop']['outgoing-interface']))
    except:
        print("\n{:14} {:20}".format(routes['destination-prefix'], routes['next-hop']['next-hop-address']))



