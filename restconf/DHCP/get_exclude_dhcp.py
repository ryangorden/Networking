import requests
from requests.auth import HTTPBasicAuth


server= "https://10.10.20.48/"
resource="restconf/data/Cisco-IOS-XE-native:native/ip/dhcp/excluded-address/"
url= f"{server}{resource}"

headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

auth= HTTPBasicAuth("developer", "C1sco12345")


requests.packages.urllib3.disable_warnings()
resp= requests.get(url, headers=headers, auth=auth, verify=False)

print(resp.text)