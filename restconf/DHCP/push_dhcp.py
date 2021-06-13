import requests
from requests.auth import HTTPBasicAuth
from yaml import safe_load
from jinja2 import Environment, FileSystemLoader
import json



def get_vars(file_path):
    with open(file_path, 'r'): as data_vars:
        vars= safe_load(data_vars)
    return vars


def template_payload(template_name,vars):
    env= Environment(loader=FileSystemLoader("."))
    template= env.get_template(template_name)
    payload= template.render(vars)

    return payload
