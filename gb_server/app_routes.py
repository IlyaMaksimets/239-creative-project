from flask import Blueprint, session, request, abort

from db_functions import *

simple_page = Blueprint('simple_page', __name__)


@simple_page.route('/', methods=['GET'])
def main_page():
    if 'login' in session:
        return session['login']
    abort(401)


@simple_page.route('/login', methods=['POST'])
def login_page():
    if 'login' in session:
        abort(400)

    login = request.json['username']
    password = request.json['password']

    user_exists = check_for_user({"login": login, "password": password})

    if user_exists is not None:
        session['login'] = login
        session['password'] = password
        return {"status": 200, "token": user_exists}

    else:
        abort(400)


@simple_page.route('/register', methods=['POST'])
def register_page():
    if 'login' in session:
        abort(400)

    login = request.json['login']
    password = request.json['password']
    passwordConfirmation = request.json['passwordConfirmation']

    user_exists = check_for_user({"login": login, "password": password})

    if not user_exists and password == passwordConfirmation:
        session['login'] = login
        session['password'] = password
        create_user({"login": login, "password": password})
        return '-created-'

    else:
        abort(400)


@simple_page.route('/logout', methods=['POST'])
def logout_page():
    session.pop('login', None)
    return '-session-finished-'


@simple_page.route('/change_avatar', methods=['POST'])
def change_avatar_page():
    return "-changed-"


@simple_page.route('/change_settings', methods=['POST'])
def change_settings_query():
    song_volume = request.json["song_volume"]
    sounds_volume = request.json["sounds_volume"]
    move_left = request.json["move_left"]
    move_right = request.json["move_right"]
    move_up = request.json["move_up"]
    move_down = request.json["move_down"]
    jump = request.json["jump"]
    pause = request.json["pause"]
    change_settings(
        {"song_volume": song_volume, "sounds_volume": sounds_volume, "move_left": move_left, "move_right": move_right,
         "move_up": move_up, "move_down": move_down, "jump": jump, "pause": pause})


@simple_page.route('/add_completion', methods=['POST'])
def add_completion_query():
    login = request.json["username"]
    level = request.json["level"]
    difficulty = request.json["difficulty"]
    stars = request.json["stars"]
    time = request.json["time"]
    add_completion({"login": login, "level": level, "difficulty": difficulty, "stars": stars, "time": time})


@simple_page.route('/get_completions', methods=['POST'])
def get_completions_query():
    return get_completions({"login": request.json["username"]})


@simple_page.route('/get_settings', methods=['POST'])
def get_settings_query():
    return get_settings({"login": request.json["username"]})
