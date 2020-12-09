from scrapli_netconf.driver import NetconfScrape

my_device={"host": "10.10.20.100",
           "auth_username": "developer",
           "auth_password": "C1sco12345",
           "auth_strict_key": False,
           "port": 830}

conn= NetconfScrape(**my_device)
conn.open()

interface_filter= """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"  xmlns:if="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>
    <name>Vlan500</name>
    <description></description>
  </interface>
</interfaces>
"""

response= conn.get(filter_=interface_filter, filter_type='subtree')
print(response.result)
