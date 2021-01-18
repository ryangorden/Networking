from dnacentersdk import api

def main():
    dnac= api.DNACenterAPI(base_url="https://sandboxdnac.cisco.com",
                           username="devnetuser",
                           password="Cisco123!")

    devices= dnac.devices.get_device_list()

    for device in devices["response"]:
       print(f"ID: {device['id']} IP: {device['managementIpAddress']}")

if __name__ =='__main__':
    main()
