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

    user_exists = check_for_user(username, password)

    if user_exists:
        session['username'] = username
        session['password'] = password
        return '-authorized-'

    else:
        abort(400)


@simple_page.route('/register', methods=['POST'])
def register_page():
    if 'username' in session:
        abort(400)

    username = request.json['username']
    password = request.json['password']
    passwordConfirmation = request.json['passwordConfirmation']

    user_exists = check_for_user(username, password)

    if not user_exists and password == passwordConfirmation:
        session['username'] = username
        session['password'] = password
        create_new_user(username, password)
        return '-created-'

    else:
        abort(400)


@simple_page.route('/logout', methods=['POST'])
def logout_page():
    session.pop('username', None)
    return '-session-finished-'


@simple_page.route('/change_avatar', methods=['POST'])
def change_avatar_page():
    return "-changed-"


@simple_page.route('/update_settings', methods=['POST'])
def update_settings_query():
    pass


@simple_page.route('/get_settings', methods=['POST'])
def get_settings_query():
    pass


@simple_page.route('/add_completion', methods=['POST'])
def add_completion_query():
    pass


@simple_page.route('/get_completions', methods=['POST'])
def get_completions_query():
    pass
