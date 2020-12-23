import requests
from requests.auth import HTTPBasicAuth
import json
from pprintpp import pprint
from tqdm import tqdm
import time

username= 'test'
password= 'test'

server= 'https://10.253.6.3'


auth= HTTPBasicAuth(username,password)

headers= {'Content-type': 'application/json'}

reqs_per_min = 5


def get_token(server, headers, auth):
    token_endpoint = '/dna/system/api/v1/auth/token'
    url = server + token_endpoint
    resp = requests.post(url, headers=headers, auth=auth, verify=False)
    token= json.loads(resp.text)
    return token['Token']

#get total client count
#break down into th cat. poor,fair,good for wired & wireless
def get_client_health(server,headers,tokens,mac):
    """
    This endpoint requires a querystring for timestamp. The value
    can be left blank. We used the params instead of add the query
    string to the url manually.
    """
    all_devices = '/dna/intent/api/v1/client-health'
    query_string= { "macAddress": mac, "timestamp": ""}
    url = server + all_devices
    headers['X-Auth-Token'] = tokens
    resp = requests.get(url, headers=headers, params=query_string, verify=False)
    client_health_list = resp.json()['response']
    pprint(client_health_list)




if __name__=='__main__':
    tokens = get_token(server, headers, auth)

    with open('client-mac.txt', 'r') as cli:
        mac_list= cli.read().splitlines()

    for i, mac in enumerate(mac_list):
        get_client_health(server,headers,tokens,mac)
        if (i +1) % reqs_per_min ==0:
            print("**** Sleeping for 1 minute to avoid API throttle ****")
            for _ in tqdm(range(60)):
                time.sleep(1)
            print()
