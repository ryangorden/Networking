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


def event_notification(server,headers,tokens):
    event_endpoint = '/dna/intent/api/v1/events?tags=ASSURANCE'
    url = server + event_endpoint
    headers['X-Auth-Token'] = tokens
    resp = requests.get(url, headers=headers, verify=False)
    event_notice = resp.json() #['response']
    pprint(event_notice)

def sub_notice(server,headers,tokens,payload):
    event_endpoint = '/dna/intent/api/v1/event/subscription'
    url = server + event_endpoint
    headers['X-Auth-Token'] = tokens
    resp = requests.post(url, headers=headers,data=json.dumps(payload), verify=False)
    print(resp.status_code)
    pprint(resp.json())



if __name__=='__main__':
    tokens = get_token(server, headers, auth)
    event_notification(server,headers,tokens)
    events_list= ['NETWORK-NON-FABRIC_WIRED-1-250','NETWORK-DEVICES-2-201']
    payload= [
    {
        "name": "TFMX sub",
        "subscriptionEndpoints": [
            {
                "subscriptionDetails": {
                    "connectionType": "REST",
                    "name": "My Flask App",
                    "description": "ingest payload into Hard Drive",
                    "method": "POST",
                    "url": "https://18.222.226.251/webhook"
                }
            }
        ],
        "filter": {
            "eventIds": events_list
        }
    }
]
    webhook= sub_notice(server,headers,tokens,payload)

