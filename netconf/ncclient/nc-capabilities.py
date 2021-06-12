from ncclient import manager

# This is making the connection to the device via ssh netconf
my_device= {"host": "10.10.20.58",
            "port": 830,
            "username": "admin",
            "password": "Cisco123",
            "hostkey_verify": False,
            "allow_agent": False,
            "look_for_keys": False,
            "device_params": {"name": "nexus"}
            }

device= manager.connect(**my_device)

# device= manager.connect(host="10.10.20.100", port=830,
#                          username="developer", password="C1sco12345",
#                         hostkey_verify=False, device_params={},
#                         allow_agent=False, look_for_keys=False)

# we are see what method are available for the managr
for abilities in device.server_capabilities:
    print(abilities)

# exiting from device
device.close_session()
