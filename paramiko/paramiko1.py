import paramiko, time

connection= paramiko.SSHClient()

connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connection.connect('10.102.30.1', username= 'username', password= 'password',
                   look_for_keys=False, allow_agent=False)

new_connection= connection.invoke_shell()
output= new_connection.recv(5000)
print(output)

new_connection.send('show version | include V\n')

time.sleep(3)

output= new_connection.recv(5000)
print(output)

new_connection.close()
