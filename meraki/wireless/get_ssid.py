import requests
import xmltodict
from pprintpp import pprint
import json

def get_org(key):
    base_server= "https://api.meraki.com/api/v1"
    endpoint= "/organizations/"

    url = f"{base_server}{endpoint}"

    headers = {
      'X-Cisco-Meraki-API-Key': key,
      'Accept': 'application/json',
      'Content-Type': 'application/json'
       }

    resp = requests.get(url, headers=headers).json()


    print("\nName                                         id")
    print("\n-----------------------------------------    -------------------- ")

    for company in resp:
        print("\n{:35}          {:20}".format(company['name'],company['id']))





def get_network(orgID,key):
    base_server="https://api.meraki.com/api/v1"
    endpoint= f"/organizations/{orgID}/networks/"

    url= f"{base_server}{endpoint}"


    headers = {
      'X-Cisco-Meraki-API-Key': key,
      'Accept': 'application/json',
      'Content-Type': 'application/json'
       }

    resp = requests.get(url, headers=headers).json()

    pprint(resp[0]['id'])



def get_ssids(networkId, key):
    base_server="https://api.meraki.com/api/v1"
    endpoint= f"/networks/{networkId}/wireless/ssids/"

    url= f"{base_server}{endpoint}"


    headers = {
      'X-Cisco-Meraki-API-Key': key,
      'Accept': 'application/json',
      'Content-Type': 'application/json'
       }

    resp = requests.get(url, headers=headers)

    pprint(resp.text)



def get_ssid(networkId, ssid_num, key):
    base_server="https://api.meraki.com/api/v1"
    endpoint= f"/networks/{networkId}/wireless/ssids/{ssid_num}"

    url= f"{base_server}{endpoint}"


    headers = {
      'X-Cisco-Meraki-API-Key': key,
      'Accept': 'application/json',
      'Content-Type': 'application/json'
       }

    resp = requests.get(url, headers=headers)

    pprint(resp.text)






if __name__ == "__main__":
    # with open("creds/creds.xml") as file:
    #     cred_dict= xmltodict.parse(file.read())
    #     key = cred_dict["api_key"]

    key="c5fabaf9a806f8861fb99b3bf0ed820d73001c92"
    org= get_org(key)
    orgID= input("Enter id for company here: ")
    get_network(orgID,key)


    networkId= input("Enter your network ID: ")
    ssid_num= 1
    get_ssids(networkId, key)
