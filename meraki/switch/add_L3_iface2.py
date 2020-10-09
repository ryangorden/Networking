import meraki
import pyAesCrypt
import json
import os

def decrypt_key(password):
    print('Getting Credentials')
    bufferSize = 64 * 1024
    clear_text_file = input('Enter unencrypted file name: ')
    secured_text_file = input('Enter encrypted file name: ')
    pyAesCrypt.decryptFile(secured_text_file, clear_text_file, password, bufferSize)
    with open(clear_text_file, 'r') as keys:
        api_key = json.load(keys)
    os.remove(clear_text_file)
    print('File has been unencrypted, extracting keys')
    print("Unencrypted file has been deleted and key has been extracted!")
    return api_key['X-Cisco-Meraki-API-Key']

def create_L3_iface(dashboard,file,serial):
    with open(file, 'r') as vars:
        L3_iface = json.load(vars)

    name = L3_iface['L3_interfaces']['name']
    interface_ip = L3_iface['L3_interfaces']['interfaceIp']
    vlan_id = L3_iface['L3_interfaces']['vlanId']
    response = dashboard.switch.createDeviceSwitchRoutingInterface(
        serial, name, interface_ip, vlan_id,
        subnet=L3_iface['L3_interfaces']['subnet'],
        multicastRouting=L3_iface['L3_interfaces']['multicastRouting']
    )
    print(response)

if __name__ == '__main__':
    apikey= decrypt_key(password)
    dashboard= meraki.DashboardAPI(apikey)
    file= input('Enter variable json file name: ')
    serial= input('Enter serial number for device')
    create_L3_iface(dashboard, file, serial)
