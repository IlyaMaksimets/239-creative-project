import json

import requests

from .utils import url


def update_level(data):
    token = open('token.txt', 'r').readlines()[0]
    requests.post(url('/add_completion'), data=json.dumps({**data, "token": token}))


def update_settings(data):
    token = open('token.txt', 'r').readlines()[0]
    requests.post(url('/change_settings'), data=json.dumps({**data, "token": token}))


def login(data):
    response = requests.post(url('/login'), data=json.dumps(data)).json()
    if response["status"] == 200:
        token = open('token.txt', 'w')
        token.write(response["token"])
        token.close()
        return True
    else:
        return False
