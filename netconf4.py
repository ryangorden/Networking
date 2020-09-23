from ncclient import manager
from lxml import etree
import xmltodict


device= manager.connect(host="ios-xe-mgmt-latest.cisco.com", port=10000,
                         username="developer", password="C1sco12345",
                        hostkey_verify=False, device_params={},
                        allow_agent=False, look_for_keys=False)


netconf_filter = """
 <filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces-state>
</filter>
"""

config= device.get_config('running', netconf_filter)

#print(type(config))
#print(type(config.data))
#print(type(config.data_ele))


#This is a way to turn the congfig xml to xml string
config_to_string= config.xml
print(xml_to_string)

