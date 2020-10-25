import pexpect



password= 'Password'
devices= [{'prompt': 'User_mode_prompt', 'ip': '10.234.40.1'},
          {'prompt': 'User_mode_prompt', 'ip': '10.234.40.10'}]

for device in devices:
    device_prompt= device['prompt']
    child= pexpect.spawn('telnet ' + device['ip'])
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt)
    child.sendline('show version | include V')
    child.expect(device['prompt'])
    print(child.before)
    print(child.after)
    child.sendline('exit')


