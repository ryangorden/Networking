from ncclient import manager


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

# getting running config for int Gi2
config= device.get_config('running', netconf_filter)


#writing int Gi2 config to a file
with open('devnet2.txt', 'w') as csr:
    csr.write(str(config))
