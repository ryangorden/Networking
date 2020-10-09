import meraki
import xmltodict
import pyAesCrypt
import os
import sys


def decrypt_key(password):
    print('Getting Credentials')
    bufferSize = 64 * 1024
    clear_text_file = input('Enter unencrypted file name: ')
    secured_text_file = input('Enter encrypted file name: ')
    pyAesCrypt.decryptFile(secured_text_file, clear_text_file, password, bufferSize)
    with open(clear_text_file, 'r') as keys:
        api_key= xmltodict.parse(keys.read())
    os.remove(clear_text_file)
    print('File has been unencrypted, extracting keys')
    print("Unencrypted file has been deleted and key has been extracted!")
    return api_key['X-Cisco-Meraki-API-Key']

def access_update_ports(dashboard,serial,port_id):
    response = dashboard.switch.updateDeviceSwitchPort(
        serial, port_id,

        enabled=True,
        type='access',
        vlan=40,
        voiceVlan=110,
        poeEnabled=True,
        linkNegotiation='Auto negotiate'
    )

    print(response)

if __name__ == '__main__':
    password = sys.argv[1]
    apikey= decrypt_key(password)
    dashboard= meraki.DashboardAPI(apikey)
    serial= input('Enter the device serial number: ')
    for port_id in range(1,49):
        access_update_ports(dashboard,serial,port_id)