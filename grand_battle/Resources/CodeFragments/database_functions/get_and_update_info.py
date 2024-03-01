from Resources.CodeFragments.database_functions.db_connections import create_test_connection
from .get_info_queries import get_info_query_1, get_info_query_2, get_info_query_3, get_info_query_4, get_info_query_5
from .update_queries import update_level_stars_info_query, update_song_volume_query, update_sounds_volume_query
from .update_queries import update_level_time_info_query1, update_level_time_info_query2
from .update_queries import update_level_time_info_query3, update_level_time_info_query4


def update_db(data):
    db_connection = create_test_connection()
    data = update_level_stars_info_query(data, db_connection)
    data = update_song_volume_query(data, db_connection)
    data = update_sounds_volume_query(data, db_connection)
    data = update_level_time_info_query1(data, db_connection)
    data = update_level_time_info_query2(data, db_connection)
    data = update_level_time_info_query3(data, db_connection)
    data = update_level_time_info_query4(data, db_connection)

    return data


def get_song_and_sounds_volume():
    db_connection = create_test_connection()
    SONG_VOLUME = 0
    SOUNDS_VOLUME = 0
    get_info_query1 = "SELECT * FROM `song-volume`"
    with db_connection.cursor() as cursor:
        cursor.execute(get_info_query1)
        result1 = cursor.fetchall()
        for (volume_level_id, condition) in result1:
            if condition[:2] == "on":
                SONG_VOLUME += 10

    get_info_query2 = "SELECT * FROM `sounds-volume`"
    with db_connection.cursor() as cursor:
        cursor.execute(get_info_query2)
        result2 = cursor.fetchall()
        for (volume_level_id, condition) in result2:
            if condition[:2] == "on":
                SOUNDS_VOLUME += 10

    return SONG_VOLUME, SOUNDS_VOLUME


def get_db_info_WOquery5():
    db_connection = create_test_connection()
    data = get_info_query_1(db_connection) + get_info_query_2(db_connection) + get_info_query_3(
        db_connection) + get_info_query_4(db_connection)
    endless_info = open('../Other/endless_record.txt')
    record = endless_info.readlines()
    endless_info.close()
    data.append(record[0])

    return data


def get_db_info(keybinds):
    db_connection = create_test_connection()
    data = get_info_query_1(db_connection) + get_info_query_2(db_connection) + get_info_query_3(
        db_connection) + get_info_query_4(db_connection)
    keybinds = get_info_query_5(db_connection, keybinds)
    endless_info = open('../Other/endless_record.txt')
    record = endless_info.readlines()
    endless_info.close()
    data.append(record[0])

    return data, keybinds
