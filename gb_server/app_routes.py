from flask import Blueprint, session, request, abort

from db_functions import *

simple_page = Blueprint('simple_page', __name__)


@simple_page.route('/', methods=['GET'])
def main_page():
    if 'username' in session:
        return session['username']
    abort(401)


@simple_page.route('/login', methods=['POST'])
def login_page():
    if 'username' in session:
        abort(400)

    username = request.json['username']
    password = request.json['password']

    user_exists = check_for_user({"username": username, "password": password})

    if user_exists:
        session['username'] = username
        session['password'] = password
        create_token(get_user_id_by_login(username))
        return {"status": 200, "token": get_token_by_user_id(get_user_id_by_login(username))}
    else:
        if 'game_login' in request.json.keys():
            return {"status": 400}
        else:
            abort(400)


@simple_page.route('/register', methods=['POST'])
def register_page():
    if 'username' in session:
        abort(400)

    login = request.json['username']
    password = request.json['password']
    passwordConfirmation = request.json['passwordConfirmation']

    user_exists = check_for_user({"login": login, "password": password})

    if not user_exists and password == passwordConfirmation:
        session['username'] = login
        session['password'] = password
        create_user({"login": login, "password": password})
        return '-created-'

    else:
        abort(400)


@simple_page.route('/logout', methods=['POST'])
def logout_page():
    session.pop('username', None)
    return '-session-finished-'


@simple_page.route('/change_settings', methods=['POST'])
def change_settings_query():
    change_settings(request.json)
    return {"status": 200}


@simple_page.route('/add_completion', methods=['POST'])
def add_completion_query():
    add_completion(request.json)
    return {"status": 200}


@simple_page.route('/get_completions', methods=['POST'])
def get_completions_query():
    if len(request.json["token"]) < 2 * TOKEN_HALF_LENGTH:
        return {}
    else:
        if "username" not in session:
            return {"data": get_completions({"token": request.json["token"]})}
        else:
            return {"data": get_completions({"username": session['username']})}


@simple_page.route('/get_settings', methods=['POST'])
def get_settings_query():
    if len(request.json["token"]) < 2 * TOKEN_HALF_LENGTH:
        return {}
    else:
        return {"data": get_settings({"token": request.json["token"]})}
