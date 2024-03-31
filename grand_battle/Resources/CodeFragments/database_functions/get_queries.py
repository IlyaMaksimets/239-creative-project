import requests

from .utils import url


def get_levels(data):
    token = open('token.txt', 'r').readlines()[0]
    res = requests.post(url('/get_completions'), json={**data, "token": token})
    if res.json() == {}:
        return None
    else:
        return res.json()['data']


def get_settings(data):
    token = open("token.txt", 'r').readlines()
    if len(token):
        token = token[0]
    res = requests.post(url('/get_settings'), json={**data, "token": token})
    if res.json() == {}:
        return None
    else:
        return res.json()['data']


def get_data(data):
    res = ["\n" for _ in range(208)]
    res[207] = "0"
    for i in range(40):
        if i % 10 == 9:
            continue
        res[i] = "0\n"

    for i in range(62, 207):
        if i % 4 == 1:
            continue
        res[i] = "00\n"

    levels = get_levels(data)
    settings = get_settings(data)
    if levels is None:
        return None
    for level in levels:
        if level["level"] == 0:
            res[207] = str(level["stars"])
            continue
        res[level["difficulty"] * 10 + level["level"] - 1] = str(level["stars"]) + '\n'
        time = level["time"].split(":")
        index = 62 + 36 * level["difficulty"] + (level["level"] - 1) * 4
        res[index] = str(time[0])
        res[index + 1] = str(time[1])
        res[index + 2] = str(time[2])

    for i in range(0, settings["song_volume"], 10):
        res[40 + i // 10] = "on\n"
    for i in range(settings["song_volume"], 100, 10):
        res[40 + i // 10] = "off\n"

    for i in range(0, settings["sounds_volume"], 10):
        res[51 + i // 10] = "on\n"
    for i in range(settings["sounds_volume"], 100, 10):
        res[51 + i // 10] = "off\n"

    return res


def get_data_and_keys(data):
    settings = get_settings(data)
    res = get_data(data)
    keybinds = dict()
    for key in settings.keys():
        if key == 'bg_enabled':
            continue
        keybinds[key] = settings[key]
    keybinds['shoot'] = "LMB"
    return [res, keybinds, settings['bg_enabled']]
