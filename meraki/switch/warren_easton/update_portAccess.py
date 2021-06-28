import requests
import json
import time

serial= "Q2EX-8W8H-39HZ"


headers= {"X-Cisco-Meraki-API-Key": "c5fabaf9a806f8861fb99b3bf0ed820d73001c92",
          "Accept": "application/json",
          "Content-Type": "application/json"}

base_url= "https://api.meraki.com/api/v1"
port_endpoint =f"/devices/{serial}/switch/ports"



null= "null"

# payload= {
#   "name": "Access Port",
#   "enabled": True,
#   "poeEnabled": True,
#   "type": "access",
#   "vlan": 108,
#   "voiceVlan": 269,
#   "isolationEnabled": False,
#   "rstpEnabled": True,
# }

payload= {
  "enabled": True,
  "poeEnabled": True,
  "type": "access",
  "vlan": 40,
  "voice vlan": null,
  "isolationEnabled": False,
  "rstpEnabled": True
}
# p= {"enabled": True,
#     "poeEnabled": True}

for portId in range(1,21):
    resp= requests.put(url=f"{base_url}{port_endpoint}/{portId}", headers=headers, data=json.dumps(payload))
    url = f"{base_url}{port_endpoint}/{portId}"
    print(url)
    print(portId)
    print(resp.status_code)
# print("Delay for 10 seconds")
# time.sleep(10)
#
# for portId in range(33,37):
#     resp= requests.put(url=f"{base_url}{port_endpoint}/{portId}", headers=headers, data=json.dumps(p))
#     print(resp.status_code)
# print("Delay for 10 seconds")
# time.sleep(10)
# for portId in range(9,11):
#     resp= requests.put(url=f"{base_url}{port_endpoint}/{portId}", headers=headers, data=json.dumps(payload))
#     print(resp.status_code)
# print("Delay for 10 seconds")
# time.sleep(10)
# for portId in range(9,11):
#     resp= requests.put(url=f"{base_url}{port_endpoint}/{portId}", headers=headers, data=json.dumps(p))
#     print(resp.status_code)

# resp= requests.get(url=f"{base_url}{port_endpoint}/{25}", headers=headers)
# print(resp.text)
