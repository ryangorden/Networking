import requests
import xmltodict
from pprintpp import pprint

def get_org(key, payload):
    base_server= "https://api.meraki.com/api/v1"
    endpoint= "/organizations/"

    url = f"{base_server}{endpoint}"

    headers = {
      'X-Cisco-Meraki-API-Key': key,
      'Accept': 'application/json',
      'Content-Type': 'application/json'
       }

    resp = requests.post(url, headers=headers,data= payload)

    return resp.text




if __name__ == "__main__":
    with open("creds/creds.xml") as file:
        cred_dict= xmltodict.parse(file.read())
        key = cred_dict["api_key"]
    payload = {"name": "Warren Easton"}


    org= get_org(key,payload)
    pprint(org)
