from ncclient import manager
import xmltodict

# This is making the connection to the device via ssh netconf
my_device= {"host": "ios-xe-mgmt.cisco.com",
            "port": 10000,
            "username": "developer",
            "password": "C1sco12345",
            "hostkey_verify": False,
            "allow_agent": False,
            "look_for_keys": False,
            "device_params": {}
            }

interface_filter= """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"  xmlns:if="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
</filter>
"""
device= manager.connect(**my_device)

netconf_response= device.get(interface_filter)

python_response= xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"]
config_response= python_response["interfaces"]["interface"]

print("all interface details")
print(config_response)
print(' ')
print("Interface Name")
print(config_response["name"]["#text"])
# exiting from device
device.close_session()
