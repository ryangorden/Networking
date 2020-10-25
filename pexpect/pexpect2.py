import pexpect

# Connection to Hynes school
child= pexpect.spawn('telnet 10.234.40.1')

child.expect('Password')
child.sendline('#BlessedNOLA')
child.expect('HYNES_4507>')
child.sendline('enable')
child.expect('Password')
child.sendline('#BlessedNOLA')

child.expect('HYNES_4507#')
child.sendline('show version')
print(child.before)
print(child.after)
child.sendline('exit')

