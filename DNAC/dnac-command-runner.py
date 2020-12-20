import requests
from requests.auth import HTTPBasicAuth
import json
from pprintpp import pprintn

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

def get_device_id(server,headers,tokens,device_id_list= []):
    all_devices = '/dna/intent/api/v1/network-device?family=Switches and Hubs&type=Cisco Catalyst 9300 Switch'
    url = server + all_devices
    headers['X-Auth-Token'] = tokens
    resp = requests.get(url, headers=headers, verify=False)
    device_list = resp.json()['response']
    device_id_list= []
    for value in device_list:
        device_id_list.append(value['id'])
    return device_id_list


def command_runner(server,headers,tokens,payload):
    runner_endpoint = '/dna/intent/api/v1/network-device-poller/cli/read-request'
    url = server + runner_endpoint
    headers['X-Auth-Token'] = tokens
    resp = requests.post(url, headers=headers,data=json.dumps(payload), verify=False)
    runner_list = resp.json()
    task_id= runner_list['response']['taskId']
    return task_id



def get_task_by_id(server,headers,tokens,task_id):
    task_id_endpoint = f'/dna/intent/api/v1/task/{task_id}'
    url = server + task_id_endpoint
    headers['X-Auth-Token'] = tokens
    resp = requests.get(url, headers=headers, verify=False)
    task_id_data = resp.json()
    data= task_id_data['response']['data']
    return data


if __name__=='__main__':
    tokens = get_token(server, headers, auth)
    print(tokens)
    exit()
    device_id_list= get_device_id(server,headers,tokens)

    payload= {
        'commands': ['show cdp nei',
                     'show ip int br'
                    ],
        'deviceUuids': device_id_list
              }
    task_id= command_runner(server,headers,tokens,payload)
    data= get_task_by_id(server,headers,tokens,task_id)
    print(data)
