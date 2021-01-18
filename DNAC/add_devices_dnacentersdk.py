from dnacentersdk import api
import time

def main():
    dnac= api.DNACenterAPI(base_url="https://sandboxdnac.cisco.com",
                           username="devnetuser",
                           password="Cisco123!")

    payload= {
    "cliTransport": "ssh",
    "enablePassword": "TFMX",
    "ipAddress": [ "192.168.1.1" ],
    "password": "cisco12345",
    "snmpROCommunity": "readonly",
    "snmpRWCommunity": "readwrite",
    "snmpRetry": 1,
    "snmpTimeout": 60,
    "snmpVersion": "v2",
    "userName": "ryangorden"}


    add_data= dnac.devices.add_device(**payload)

    time.sleep(10)
    task= add_data["response"]["taskId"]
    task_data= dnac.task.get_task_by_id(task)

    if not task_data["response"]["isError"]:
        print("New device sucessfully added")
    else:
        print(f"Async task error seen: {task_data['progress']}")

if __name__ =='__main__':
    main()
