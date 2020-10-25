import pexpect

devices= { 'core_switch': {'prompt': 'HYNES4507>', 'ip': '10.234.40.1'},
           'access_switch': {'prompt': 'HYNES3750>', 'ip': '10.234.40.10'}}

for device in devices.keys():
    device_prompt= device['prompt']
    print(device_prompt)
