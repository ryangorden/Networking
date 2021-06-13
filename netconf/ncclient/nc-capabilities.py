from ncclient import manager

# This is making the connection to the device via ssh netconf
my_device= {"host": "10.10.20.48",
            "port": 830,
            "username": "developer",
            "password": "C1sco12345",
            "hostkey_verify": False,
            "allow_agent": False,
            "look_for_keys": False,
            "device_params": {}
            }

with manager.connect(**my_device) as device:



    # we are see what method are available for the managr
    for abilities in device.server_capabilities:
        print("*" * 50)
        print(abilities)
        print("*" * 50)

    # exiting from device
    device.close_session()
