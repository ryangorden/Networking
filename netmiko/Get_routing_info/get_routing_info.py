from yaml import safe_load
from netmiko import ConnectHandler

#Read in host file into structed data
with open("hosts.yml", "r") as file:
    host_root= safe_load(file)


with open("commands.yml", "r") as file:
    commands= safe_load(file)

for profile in host_root["Production"]:
    connection= ConnectHandler(**profile)
    print("Connected to device: " + profile["ip"])
    for command in commands["commands"]:
        sent_command= connection.send_command(command)
        print(sent_command)
        print("-" * len(sent_command))
    connection.disconnect()
