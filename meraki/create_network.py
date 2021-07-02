import requests
import xmltodict
from pprintpp import pprint

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



def create_network(orgID,key,payload):
    base_server="https://api.meraki.com/api/v1"
    endpoint= f"/organizations/{orgID}/networks/"

    url= f"{base_server}{endpoint}"


    headers = {
      'X-Cisco-Meraki-API-Key': key,
      'Accept': 'application/json',
      'Content-Type': 'application/json'
       }

    resp = requests.post(url, headers=headers,data=payload)

    pprint(resp.text)


if __name__ == "__main__":
    with open("creds/creds.xml") as file:
        cred_dict= xmltodict.parse(file.read())
        key = cred_dict["api_key"]
    org= get_org(key)
    orgID= input("Enter id for company here: ")
 

    payload= {
    "name": "Warren Easton High School",
    "productTypes": [
        "wireless",
        "switch"
                    ]
            }
    create_network(orgID,key,payload)
