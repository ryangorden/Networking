import requests
from requests.auth import HTTPBasicAuth


server= "https://10.10.20.48/"
resource="restconf/data/ietf-interfaces:interfaces/interface"
param="=Loopback500"

url= f" {server}{resource}{param}"



headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

auth= HTTPBasicAuth("developer", "C1sco12345")
resp= requests.delete(url, headers=headers, auth=auth, verify=False)

print(resp.text)