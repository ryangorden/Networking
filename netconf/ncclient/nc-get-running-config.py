from ncclient import manager
import xmltodict
from pprintpp import pprint

device= manager.connect(host="ios-xe-mgmt.cisco.com", port=10000,
                         username="developer", password="C1sco12345",
                        hostkey_verify=False, device_params={},
                        allow_agent=False, look_for_keys=False)

# Retrieving the running configurations
config= device.get_config('running')

python_response= config.xml

pprint(xmltodict.parse(python_response)['rpc-reply']['data'])


