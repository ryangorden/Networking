import requests
from requests.auth import HTTPBasicAuth

url = "https://10.10.20.100:443/restconf/data/openconfig-vlan:vlans/vlan=4000"

headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json'
}

auth= HTTPBasicAuth("developer", "C1sco12345")
requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=headers, auth=auth, verify=False)

print(response.text)
