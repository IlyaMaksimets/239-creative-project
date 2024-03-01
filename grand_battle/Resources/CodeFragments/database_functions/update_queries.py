from Resources.CodeFragments.database_functions.db_connections import create_test_connection


def update_song_volume_query(data, db_connection):
    for i in range(40, 50):
        update_query = "UPDATE `song-volume` SET `condition`=\'" + data[i][:-1] + "\' WHERE volume_level_id=" + str(
            (i % 10) + 1)
        with db_connection.cursor() as cursor:
            cursor.execute(update_query)
            db_connection.commit()

    return data


def update_sounds_volume_query(data, db_connection):
    for i in range(51, 61):
        update_query = "UPDATE `sounds-volume` SET `condition`=\'" + data[i][:-1] + "\' WHERE volume_level_id=" + str(
            i - 50)
        with db_connection.cursor() as cursor:
            cursor.execute(update_query)
            db_connection.commit()

    return data


def update_level_stars_info_query(data, db_connection):
    for i in range(9):
        update_query = "UPDATE `levels-info` SET stars=" + data[
            i] + " WHERE difficulty=\"beginner\" AND level=" + str((i % 10) + 1)
        with db_connection.cursor() as cursor:
            cursor.execute(update_query)
            db_connection.commit()
    for i in range(10, 19):
        update_query = "UPDATE `levels-info` SET stars=" + data[i] + " WHERE difficulty=\"medium\" AND level=" + str(
            (i % 10) + 1)
        with db_connection.cursor() as cursor:
            cursor.execute(update_query)
            db_connection.commit()
    for i in range(20, 29):
        update_query = "UPDATE `levels-info` SET stars=" + data[i] + " WHERE difficulty=\"hard\" AND level=" + str(
            (i % 10) + 1)
        with db_connection.cursor() as cursor:
            cursor.execute(update_query)
            db_connection.commit()
    for i in range(30, 39):
        update_query = "UPDATE `levels-info` SET stars=" + data[i] + " WHERE difficulty=\"insane\" AND level=" + str(
            (i % 10) + 1)
        with db_connection.cursor() as cursor:
            cursor.execute(update_query)
            db_connection.commit()

    return data


def update_level_time_info_query1(data, db_connection):
    for i in range(62, 97, 4):
        update_query1 = "UPDATE `levels-info` SET hours=\'" + data[i][
                                                              :2] + "\' WHERE difficulty=\"beginner\" AND level=" + str(
            (i - 62) / 4 + 1)
        update_query2 = "UPDATE `levels-info` SET minutes=\'" + data[i + 1][
                                                                :2] + "\' WHERE difficulty=\"beginner\" AND level=" + str(
            (i - 62) / 4 + 1)
        update_query3 = "UPDATE `levels-info` SET seconds=\'" + data[i + 2][
                                                                :2] + "\' WHERE difficulty=\"beginner\" AND level=" + str(
            (i - 62) / 4 + 1)
        with db_connection.cursor() as cursor:
            cursor.execute(update_query1)
            db_connection.commit()
        with db_connection.cursor() as cursor:
            cursor.execute(update_query2)
            db_connection.commit()
        with db_connection.cursor() as cursor:
            cursor.execute(update_query3)
            db_connection.commit()

    return data


def update_level_time_info_query2(data, db_connection):
    for i in range(98, 133, 4):
        update_query1 = "UPDATE `levels-info` SET hours=\'" + data[i][
                                                              :2] + "\' WHERE difficulty=\"medium\" AND level=" + str(
            (i - 98) / 4 + 1)
        update_query2 = "UPDATE `levels-info` SET minutes=\'" + data[i + 1][
                                                                :2] + "\' WHERE difficulty=\"medium\" AND level=" + str(
            (i - 98) / 4 + 1)
        update_query3 = "UPDATE `levels-info` SET seconds=\'" + data[i + 2][
                                                                :2] + "\' WHERE difficulty=\"medium\" AND level=" + str(
            (i - 98) / 4 + 1)
        with db_connection.cursor() as cursor:
            cursor.execute(update_query1)
            db_connection.commit()
        with db_connection.cursor() as cursor:
            cursor.execute(update_query2)
            db_connection.commit()
        with db_connection.cursor() as cursor:
            cursor.execute(update_query3)
            db_connection.commit()

    return data


def update_level_time_info_query3(data, db_connection):
    for i in range(134, 169, 4):
        update_query1 = "UPDATE `levels-info` SET hours=\'" + data[
                                                                  i][
                                                              :2] + "\' WHERE difficulty=\"hard\" AND level=" + str(
            (i - 134) / 4 + 1)
        update_query2 = "UPDATE `levels-info` SET minutes=\'" + data[
                                                                    i + 1][
                                                                :2] + "\' WHERE difficulty=\"hard\" AND level=" + str(
            (i - 134) / 4 + 1)
        update_query3 = "UPDATE `levels-info` SET seconds=\'" + data[
                                                                    i + 2][
                                                                :2] + "\' WHERE difficulty=\"hard\" AND level=" + str(
            (i - 134) / 4 + 1)
        with db_connection.cursor() as cursor:
            cursor.execute(update_query1)
            db_connection.commit()
        with db_connection.cursor() as cursor:
            cursor.execute(update_query2)
            db_connection.commit()
        with db_connection.cursor() as cursor:
            cursor.execute(update_query3)
            db_connection.commit()

    return data


def update_level_time_info_query4(data, db_connection):
    for i in range(170, 205, 4):
        update_query1 = "UPDATE `levels-info` SET hours=\'" + data[
                                                                  i][
                                                              :2] + "\' WHERE difficulty=\"insane\" AND level=" + str(
            (i - 170) / 4 + 1)
        update_query2 = "UPDATE `levels-info` SET minutes=\'" + data[
                                                                    i + 1][
                                                                :2] + "\' WHERE difficulty=\"insane\" AND level=" + str(
            (i - 170) / 4 + 1)
        update_query3 = "UPDATE `levels-info` SET seconds=\'" + data[
                                                                    i + 2][
                                                                :2] + "\' WHERE difficulty=\"insane\" AND level=" + str(
            (i - 170) / 4 + 1)
        with db_connection.cursor() as cursor:
            cursor.execute(update_query1)
            db_connection.commit()
        with db_connection.cursor() as cursor:
            cursor.execute(update_query2)
            db_connection.commit()
        with db_connection.cursor() as cursor:
            cursor.execute(update_query3)
            db_connection.commit()

    return data


def update_key_in_db(keybinds, action):
    db_connection = create_test_connection()

    update_query1 = "UPDATE `key-binds` SET `key`=\"" + keybinds[action] + "\" WHERE actions=\"" + action + "\""
    with db_connection.cursor() as cursor:
        cursor.execute(update_query1)
        db_connection.commit()
