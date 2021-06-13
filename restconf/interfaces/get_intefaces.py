import requests
from requests.auth import HTTPBasicAuth

server= "https://10.10.20.48/"
resource="restconf/data/ietf-interfaces:interfaces/interface"


url= f" {server}{resource}"



headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

auth= HTTPBasicAuth("developer", "C1sco12345")

resp= requests.get(url, headers=headers, auth=auth, verify=False)

print(resp.text)