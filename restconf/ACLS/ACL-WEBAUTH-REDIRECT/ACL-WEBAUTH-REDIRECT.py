"""
This script is used to test acl creation, verify acl and
delete the acl. It has been tested with Cisco IOS version
16.9.03
"""



import json
import requests

base_server= "https://10.10.20.100"
acls_endpoint= "/restconf/data/Cisco-IOS-XE-native:native/ip/access-list/"
port= 443

url= f"{base_server}:{port}{acls_endpoint}"


headers= {"Content-Type": "application/yang-data+json",
          "Accept": "application/yang-data+json"}

# username and password
auth= ("developer","C1sco12345")

# open payload file
with open("ACL-WEBAUTH-REDIRECT.json", "r") as file:
    payload= json.load(file)


# send post requests to create a new acl
requests.packages.urllib3.disable_warnings()
resp= requests.post(url, headers=headers, auth=auth, data=json.dumps(payload), verify= False)
print(resp.status_code)

# change url endpoint to specific acl
# send get requests to only get that acl
# that we just created
acl_endpoint= "/restconf/data/Cisco-IOS-XE-native:native/ip/access-list/extended=ACL-WEBAUTH-REDIRECT"
url= f"{base_server}:{port}{acl_endpoint}"
resp= requests.get(url, headers=headers, auth=auth, verify= False)
print(resp.text)

# Delete acl we just created
resp= requests.delete(url, headers=headers, auth=auth, verify= False)
print(resp.status_code)

