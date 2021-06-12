from ncclient import manager
import xmltodict

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

# <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"  xmlns:if="urn:ietf:params:xml:ns:yang:ietf-interfaces">
interface_filter= """
<filter>
  <interfaces xmlns="http://openconfig.net/yang/interfaces">
    <interface>
    <name>Eth1/5</name>
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
