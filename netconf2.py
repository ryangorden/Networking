from ncclient import manager


device= manager.connect(host="ios-xe-mgmt-latest.cisco.com", port=10000,
                         username="developer", password="C1sco12345",
                        hostkey_verify=False, device_params={},
                        allow_agent=False, look_for_keys=False)

# Retrieving the running configurations
config= device.get_config('running')

#writing the configuration to a file
with open('devnet.txt', 'w') as csr:
    csr.write(str(config))
