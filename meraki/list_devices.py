
import requests
import meraki

meraki_key = {'X-Cisco-Meraki-API-Key': '9858888888888880'} # This is not a real key. Please change to your key.
apikey = meraki_key['X-Cisco-Meraki-API-Key']

def get_orgid(apikey):
    myOrg = meraki.myorgaccess(apikey)
    for line in myOrg:
        print(line['name'], 'id: ' + line['id'])

    orgid = input('Enter Org ID: ')
    return orgid

def get_networkid(apikey, orgid):
    myNetwork = meraki.getnetworklist(apikey, orgid)
    print(myNetwork)

    netid= input('Enter your network id: ')
    return netid

def get_device_list(url,headers):
    print(url)
    resp= requests.get(url, headers=headers).json()
    print('Getting list of devices.')
    print('\nSerial          Mac                IP              Model              Name')
    print('\n------          ----------------   --------------- -------------      -------------------')
    for device in resp:
        try:

            print('{0:14}  {1:16}  {2:15} {4:16}   {3:12}'.format(device['serial'], device['mac'], device['lanIp'], device['name'], device['model']))
        except (TypeError):
            print('{0:14}  {1:16}  {2:15} {4:16}   {3:12}'.format(device['serial'], device['mac'], 'No IP' , device['name'], device['model']))


if __name__ == '__main__':
    orgid= get_orgid(apikey)
    netid= get_networkid(apikey,orgid)


    base_url= 'https://dashboard.meraki.com/api/v0'
    resource= f'networks/{netid}/devices'

    headers = {'Content-Type': 'application/json',
               'X-Cisco-Meraki-API-Key': apikey}

    url= f'{base_url}/{resource}'

    get_device_list(url,headers)
