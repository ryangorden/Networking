import meraki
import os
from dotenv import load_dotenv
from unittest import TestCase
from pprintpp import pprint
from update_portAccess import app


class TestPort(TestCase):
    load_dotenv()
    key = os.environ.get("APIKEY")
    def test_port(self,key=key):
        dashboard= meraki.DashboardAPI(key)

        portConfig= {"vlan": 10, "portId": 11,"serial": "Q2EX-8W8H-39HZ"}
        resp = dashboard.switch.updateDeviceSwitchPort(**portConfig)

        self.assertEqual(resp['vlan'],10)

    def test_home(self):
        with app.test_client as c:
            resp= c.get('/')
            self.assertEqual(resp.status_code,200)
