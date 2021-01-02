import requests
from requests.auth import HTTPBasicAuth
import json

server= "https://10.10.20.100/"

resource="restconf/data/ietf-interfaces:interfaces/"

url= f"{server}{resource}"

headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

auth= HTTPBasicAuth("developer", "C1sco12345")

payload = {
    "ietf-interfaces:interface": {
        "name": "Vlan500",
        "description": "RG1 Test",
        "type": "iana-if-type:l3ipvlan",
        "enabled": False,
        "ietf-ip:ipv4": {"address": [{"ip": "192.168.1.1", "netmask": "255.255.255.0"}]},
        "ietf-ip:ipv6": {}
    }
}

resp= requests.post(url, headers=headers, auth=auth, data= json.dumps(payload), verify=False)


if resp.status_code == 201:
    print("yes")
    resource2="restconf/data/ietf-interfaces:interfaces/interface=Vlan500"
    url= f"{server}{resource2}"
    resp2= requests.get(url, headers=headers, auth=auth, verify=False)
    print(resp2.text)
    #resp2 = requests.delete(url, headers=headers, auth=auth, verify=False)
