import meraki
import os
from dotenv import load_dotenv
from unittest import TestCase
from pprintpp import pprint



class TestPort(TestCase):
    load_dotenv()
    key = os.environ.get("APIKEY")
    def test_port(self,key=key):
        dashboard= meraki.DashboardAPI(key)

        portConfig= {"vlan": 10, "portId": 11,"serial": "Q2EX-8W8H-39HZ"}
        resp = dashboard.switch.updateDeviceSwitchPort(**portConfig)
       # pprint(resp)
        self.assertEqual(resp['vlan'],10)
