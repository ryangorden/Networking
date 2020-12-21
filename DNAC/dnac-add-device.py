import requests
from requests.auth import HTTPBasicAuth
import json
import time
from pprintpp import pprint

username= 'devnetuser'
password= 'Cisco123!'

server= 'https://sandboxdnac.cisco.com'


auth= HTTPBasicAuth(username,password)

headers= {'Content-type': 'application/json',
          'Accept': 'application/json'}

def get_token(server, headers, auth):
    token_endpoint = '/dna/system/api/v1/auth/token'
    url = server + token_endpoint
    resp = requests.post(url, headers=headers, auth=auth, verify=False)
    token= json.loads(resp.text)
    return token['Token']

def add_device(server,headers,tokens,payload):
    all_devices = '/dna/intent/api/v1/network-device'
    url = server + all_devices
    headers['X-Auth-Token'] = tokens
    resp = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
    taskId = resp.json()['response']['taskId']
    return taskId


def get_task_info(server, headers,tokens, taskId):
    time.sleep(10)
    task_endpoint = f'/dna/system/api/v1/auth/task/{taskId}'
    url = server + task_endpoint
    resp = requests.post(url, headers=headers, verify=False)
    task= json.loads(resp.text)
    return task['response']




if __name__=='__main__':
    tokens = get_token(server, headers, auth)
    payload= {
    "cliTransport": "ssh",
    "enablePassword": "TFMX",
    "ipAddress": [ "192.168.1.1" ],
    "password": "cisco12345",
    "snmpROCommunity": "readonly",
    "snmpRWCommunity": "readwrite",
    "snmpRetry": 1,
    "snmpTimeout": 60,
    "snmpVersion": "v2",
    "userName": "ryangorden"
}
    taskId= get_device(server,headers,tokens, payload)
    display_added_device= get_task_info(server, headers,tokens, taskId)
