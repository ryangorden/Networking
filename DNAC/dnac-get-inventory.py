import requests
from requests.auth import HTTPBasicAuth
import json
from pprintpp import pprint

username= 'devnetuser'
password= 'Cisco123!'

server= 'https://sandboxdnac.cisco.com'


auth= HTTPBasicAuth(username,password)

headers= {'Content-type': 'application/json'}

def get_token(server, headers, auth):
    token_endpoint = '/dna/system/api/v1/auth/token'
    url = server + token_endpoint
    resp = requests.post(url, headers=headers, auth=auth, verify=False)
    token= json.loads(resp.text)
    return token['Token']

def get_device(server,headers,tokens):
    all_devices = '/dna/intent/api/v1/network-device'
    url = server + all_devices
    headers['X-Auth-Token'] = tokens
    resp = requests.get(url, headers=headers, verify=False)
    device_list = resp.json()
    for value in device_list['response']:
        pprint(value)




if __name__=='__main__':
    tokens = get_token(server, headers, auth)
    get_device(server,headers,tokens)
