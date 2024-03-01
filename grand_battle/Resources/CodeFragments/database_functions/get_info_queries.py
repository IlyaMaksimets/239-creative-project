def get_info_query_1(db_connection):
    get_info_query1 = "SELECT * FROM `levels-info`"
    data = []
    with db_connection.cursor() as cursor:
        cursor.execute(get_info_query1)
        result1 = cursor.fetchall()
        for (id, difficulty, level, stars, hours, minutes, seconds) in result1:
            data.append(str(stars) + '\n')
            if id % 9 == 0:
                data.append('\n')

    return data


def get_info_query_2(db_connection):
    get_info_query2 = "SELECT * FROM `song-volume`"
    data = []
    with db_connection.cursor() as cursor:
        cursor.execute(get_info_query2)
        result2 = cursor.fetchall()
        for (volume_level_id, condition) in result2:
            data.append(condition + '\n')
    data.append('\n')

    return data


def get_info_query_3(db_connection):
    data = []
    get_info_query3 = "SELECT * FROM `sounds-volume`"
    with db_connection.cursor() as cursor:
        cursor.execute(get_info_query3)
        result3 = cursor.fetchall()
        for (volume_level_id, condition) in result3:
            data.append(condition + '\n')
        data.append('\n')

    return data


def get_info_query_4(db_connection):
    data = []
    get_info_query4 = "SELECT * FROM `levels-info`"
    with db_connection.cursor() as cursor:
        cursor.execute(get_info_query4)
        result4 = cursor.fetchall()
        for (id, difficulty, level, stars, hours, minutes, seconds) in result4:
            data.append(hours + '\n')
            data.append(minutes + '\n')
            data.append(seconds + '\n')
            data.append('\n')

    return data


def get_info_query_5(db_connection, keybinds):
    get_info_query5 = "SELECT * FROM `key-binds`"
    with db_connection.cursor() as cursor:
        cursor.execute(get_info_query5)
        result5 = cursor.fetchall()
        for (action, key) in result5:
            keybinds[action] = key

    return keybinds
