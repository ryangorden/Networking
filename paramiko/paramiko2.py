import paramiko, time

devices= [{'ip': '10.102.30.1'},
          {'ip': '10.102.30.22'}]

commands= ['show version']

username= 'username'
password= 'password'

max_buffer= 65535

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


if __name__ == '__main__':
    for device in devices:
        output_FileName=  device['ip'] + '_output.txt'
        connection= paramiko.SSHClient()
        connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        connection.connect(device['ip'], username= username, password= password,
                           look_for_keys=False, allow_agent=False)

        new_connection= connection.invoke_shell()
        output= clear_buffer(new_connection)

        time.sleep(5)
        new_connection.send('terminal length 0\n')
        output= clear_buffer(new_connection)

        with open(output_FileName, 'wb') as f:
            for command in commands:
                new_connection.send(command)
                time.sleep(5)
                output= new_connection.recv(max_buffer)
                print(output)
                f.write(output)
