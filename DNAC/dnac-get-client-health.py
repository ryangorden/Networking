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

#get total client count
#break down into th cat. poor,fair,good for wired & wireless
def get_client_health(server,headers,tokens):
    """
    This endpoint requires a querystring for timestamp. The value
    can be left blank. We used the params instead of add the query
    string to the url manually.
    """
    all_devices = '/dna/intent/api/v1/client-health'
    query_string= {"timestamp": ""}
    url = server + all_devices
    headers['X-Auth-Token'] = tokens
    resp = requests.get(url, headers=headers, params=query_string, verify=False)
    client_health_list = resp.json()['response']
    pprint(client_health_list)




if __name__=='__main__':
    tokens = get_token(server, headers, auth)
    get_client_health(server,headers,tokens)
