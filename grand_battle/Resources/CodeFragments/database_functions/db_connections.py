import mysql.connector
from mysql.connector import Error


def create_test_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.2',
            user='Tremexen',
            passwd='q4h887dm_RN',
            database='grand_battle-info'
        )
    except Error:
        print(f"The error '{Error}' occurred")
    return connection


def create_emergency_connection():
    info = open('../backup_info.txt')
    data = info.readlines()[:-1]
    return data
