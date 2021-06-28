import requests
import xmltodict

with open("creds/creds.xml") as file:
    creds_dict= xmltodict.parse(file.read())



url = "https://api.meraki.com/api/v1/organizations/"


headers = {
  'X-Cisco-Meraki-API-Key': creds_dict["api_key"],
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

resp = requests.get(url, headers=headers).json()


print("\nName                                         id")
print("\n-----------------------------------------    -------------------- ")

for company in resp:
    #print(f"{company['name']}     {company['id']}")
    print("\n{:35}          {:20}".format(company['name'],company['id']))
