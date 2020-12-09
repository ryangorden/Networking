from scrapli_netconf.driver import NetconfScrape

my_device={"host": "10.10.20.100",
           "auth_username": "developer",
           "auth_password": "C1sco12345",
           "auth_strict_key": False,
           "port": 830}

conn= NetconfScrape(**my_device)
conn.open()

interface_filter_xpath= '/interfaces/interface[name="Vlan500"]/description'

response= conn.get(filter_=interface_filter_xpath, filter_type='xpath')
print(response.result)
