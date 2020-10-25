import pexpect


child= pexpect.spawn('telnet 10.125.40.1')

child.expect('Password')
child.sendline('Password')
child.expect('User_mode_prompt')
child.sendline('enable')
child.expect('Password')
child.sendline('Password')

child.expect('Enable_prompt')
child.sendline('show version')
print(child.before)
print(child.after)
child.sendline('exit')

