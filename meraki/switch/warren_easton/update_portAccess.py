import meraki
import os
from dotenv import load_dotenv
from yaml import safe_load



with open("inventory/host.yml", 'r') as host:
    switches = safe_load(host)
    serialNums = switches['meraki']['switches']['serial']

load_dotenv()
key = os.environ.get("APIKEY")



for serial in serialNums.keys():
    print(serial)
    dashboard= meraki.DashboardAPI(key)
    for porId in range(1,20)
        print("Configuring" + serial)
        if serial== "Q2AY-YH7H-TBPU" and portId in range(1,6):
            print("Configuring " + portId + " in vlan 1")
            portConfig= {"vlan": 1, "portId": portId,"serial": serial}
            resp = dashboard.switch.updateDeviceSwitchPort(**portConfig)
        else:
            print("Configuring " + portId + " in vlan 1")
            portConfig= {"vlan": 40, "voiceVlan": 110, "portId": portId,"serial": serial}
            resp = dashboard.switch.updateDeviceSwitchPort(**portConfig)
