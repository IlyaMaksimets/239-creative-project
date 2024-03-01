import secrets

import mysql.connector
from mysql.connector import Error


def create_connection(host, username, password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            passwd=password,
            database=database,
            auth_plugin='mysql_native_password'
        )
    except Error as e:
        print(e)
    return connection


def check_for_user(username, password):
    db_connection = create_connection('127.0.0.2', 'Service', 'service_password', 'users-list')
    check_info_query = f'SELECT * FROM users WHERE username="{username}" AND password="{password}";'
    cursor = db_connection.cursor()
    cursor.execute(check_info_query)
    result = cursor.fetchall()

    return len(result) > 0


def create_new_user(username, password):
    db_connection = create_connection('127.0.0.2', 'Service', 'service_password', 'users-list')
    generated_ID = secrets.token_hex(10)
    check_info_query = f'INSERT INTO users (ID, username, password) VALUES ("{generated_ID}", "{username}", "{password}");'
    cursor1 = db_connection.cursor()
    cursor1.execute(check_info_query)
    db_connection.commit()
