from yaml import safe_load
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

#Read in host file into structed data
with open("hosts.yml", "r") as file:
    host_root= safe_load(file)


with open("var/dns_var.yml", "r") as file:
    commands= safe_load(file)


def get_template(template,var):
    env= Environment(loader=FileSystemLoader('.'))
    template= env.get_template(template)
    commands= template.render(var)

    return commands



if __name__ == "__main__":
    for profile in host_root["Production"]:
        connection= ConnectHandler(**profile)
        print("Connected to device: " + profile["ip"])
        config_commands= get_template("templates/dns_template.j2", commands)
        sent_commands= connection.send_config_set(config_commands)
        print(sent_commands)
        print(connection.send_command('ping yahoo.com'))
        print(connection.send_command('ping 8.8.8.8'))
        connection.disconnect()
