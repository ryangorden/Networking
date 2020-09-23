from ncclient import manager

# This is making the connection to the device via ssh netconf
device= manager.connect(host="ios-xe-mgmt-latest.cisco.com", port=10000,
                         username="developer", password="C1sco12345",
                        hostkey_verify=False, device_params={},
                        allow_agent=False, look_for_keys=False)

# we are see what method are available for the managr
for item in dir(device):
    print(item)

# exiting from device
device.close_session()
