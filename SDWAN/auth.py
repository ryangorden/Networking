import requests
import json
import urllib3

urllib3.disable_warning(urllib3.exceptions.InsecureRequestWarning)

base_url= "https://10.10.20.90/"
auth_endpoint= "j_security_check"

login_body = {
              "j_username": "admin",
              "j_password": "C1sco12345"
             }

sesh= requests.session()
login_response= sesh.post(
    url= f"{base_url}{auth_endpoint}", data= login_body, verify=False)

if not login_response.ok or login_response.text:
    print("login failed")
    import sys
    sys.exit(1)
else:
    print("login suceeded")
