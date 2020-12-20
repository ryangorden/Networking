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




if __name__=='__main__':
    tokens = get_token(server, headers, auth)
    event_notification(server,headers,tokens)
