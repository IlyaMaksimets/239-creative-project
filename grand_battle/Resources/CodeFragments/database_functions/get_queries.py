import json

import requests

from .utils import url


def get_levels(data):
    token = open('token.txt', 'r').readlines()[0]
    res = requests.post(url('/get_completions'), json={**data, "token": token})
    if res.json() == {}:
        return None
    else:
        return res.json()


def get_settings(data):
    token = open('token.txt', 'r').readlines()[0]
    res = requests.post(url('/get_settings'), json={**data, "token": token})
    if res.json() == {}:
        return None
    else:
        return res.json()


def get_data(data):
    res = ["\n" for _ in range(208)]
    levels = get_levels(data)
    settings = get_settings(data)
    if levels is None:
        return None
    for level in levels:
        if level["difficulty"] == 4:
            res[207] = level["stars"]
            continue
        res[level["difficulty"] * 10 + level["level"] - 1] = str(level["stars"]) + '\n'
        time = level["time"].split(":")
        index = 63 + 36 * level["difficulty"] + (level["level"] - 1) * 4
        res[index] = str(time[0])
        res[index + 1] = str(time[1])
        res[index + 2] = str(time[2])

    for i in range(0, settings["song_volume"], 10):
        res[40 + i // 10] = "on"
    for i in range(settings["song_volume"], 100, 10):
        res[40 + i // 10] = "off"

    for i in range(0, settings["sounds_volume"], 10):
        res[51 + i // 10] = "on"
    for i in range(settings["sounds_volume"], 100, 10):
        res[51 + i // 10] = "off"

    print(res)
    return res


def get_data_and_keys(data):
    settings = get_settings(data)
    res = get_data(data)
    keybinds = dict()
    for key, value in settings:
        keybinds[key] = value
    return [res, settings]