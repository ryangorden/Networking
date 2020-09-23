from ncclient import manager
from lxml import etree



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

#add the .data method will give us access to the xml object
#the tostring method will let us turn the memory xml object to a string
# Adding the pretty_print arg will make the text more readable
config_string= etree.tostring(config.data, pretty_print=True)
print(config_string)

