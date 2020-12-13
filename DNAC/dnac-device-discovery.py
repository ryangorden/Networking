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

def cli_device_discover(server,headers,tokens):
    all_devices = '/dna/intent/api/v1/global-credential?credentialSubType=CLI'
    url = server + all_devices
    headers['X-Auth-Token'] = tokens
    resp = requests.get(url, headers=headers, verify=False)
    cli_creds_list = resp.json()
    cli_creds= cli_creds_list['response'][0]['id']
    return cli_creds


def snmp_device_discover(server,headers,tokens):
    all_devices = '/dna/intent/api/v1/global-credential?credentialSubType=SNMPV2_WRITE_COMMUNITY' 
    url = server + all_devices
    headers['X-Auth-Token'] = tokens
    resp = requests.get(url, headers=headers, verify=False).json()
    return resp['response'][0]['id']


def discovery(server,headers,tokens,payload):
    all_devices = '/dna/intent/api/v1/discovery'
    url = server + all_devices
    headers['X-Auth-Token'] = tokens
    resp = requests.post(url, headers=headers, data= json.dumps(payload), verify=False)
    print(resp)
    print(resp.text)

if __name__=='__main__':
    tokens = get_token(server, headers, auth)
    cli_cred= cli_device_discover(server,headers,tokens)
    snmp_cred= snmp_device_discover(server,headers,tokens)

    payload = {
               "name": "TFMX Discovery",
               "discoveryType": "Range",
               "ipAddresslist": "10.10.20.30-10.10.20.254",
               "timeout": 1,
               "protocolOrder":  "ssh,telnet",
               "preferredMgmt": "None",
               "gloabalCredentialList":[cli_cred, snmp_cred] 
              }
    disc= discovery(server,headers,tokens,payload)
