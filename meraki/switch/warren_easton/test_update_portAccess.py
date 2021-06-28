import json
import requests
from unittest import TestCase



class TestHome(TestCase):
    def test_home(self):
        headers = {"X-Cisco-Meraki-API-Key": "c5fabaf9a806f8861fb99b3bf0ed820d73001c92",
                   "Accept": "application/json",
                   "Content-Type": "application/json"}

        base_url = "https://api.meraki.com/api/v1"
        port_endpoint = f"/devices/{serial}/switch/ports"

        payload = {
            "enabled": True,
            "poeEnabled": True,
            "type": "access",
            "vlan": 40,
            "voice vlan": null,
            "isolationEnabled": False,
            "rstpEnabled": True
        }

        resp = requests.put(url=f"{base_url}{port_endpoint}/{portId}", headers=headers, data=json.dumps(payload))
        self.assertEqual(resp.status_code,201)

