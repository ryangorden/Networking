from scrapli_netconf.driver import NetconfScrape

my_device={"host": "10.10.20.100",
           "auth_username": "developer",
           "auth_password": "C1sco12345",
           "auth_strict_key": False,
           "port": 830}

conn= NetconfScrape(**my_device)
conn.open()

rpc_filter='''
<get>
  <filter xmlns:t="urn:ietf:params:xml:ns:yang:ietf-interfaces" type="xpath" select="/interfaces/interface[name='Vlan500']/description"/>
</get>
'''

response= conn.rpc(rpc_filter)
print(response.result)
