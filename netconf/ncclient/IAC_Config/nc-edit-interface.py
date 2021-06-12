from router_info import my_device
from ncclient import manager
from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

with open("filter_vars.yml", "r") as file:
    var= safe_load(file)

env= Environment(loader=FileSystemLoader("."))
template= env.get_template("filter_template.j2")
payload= template.render(var)

print(payload)
exit()
with manager.connect(**my_device) as m:
    response= m.edit_config(payload, target= "running")

print(response)



