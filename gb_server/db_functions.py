import datetime
import secrets

from cfg import TOKEN_HALF_LENGTH, SEC_IN
from models import *


def create_token(user_id):
    db.session.execute(
        db.insert(Token).values(id=secrets.token_hex(TOKEN_HALF_LENGTH), user_id=user_id, date=datetime.datetime.now()))
    db.session.commit()


def get_user_id_by_token(user_token):
    return list(db.session.execute(db.select(Token).where(Token.id == user_token)).scalars())[0].user_id


def get_token_by_user_id(user_id):
    return list(db.session.execute(db.select(Token).where(Token.user_id == user_id)).scalars())[0].id


def get_user_id_by_login(username):
    return list(db.session.execute(db.select(User).where(User.login == username)).scalars())[0].id


def check_for_user(data):
    user_in_db = list(db.session.execute(
        db.select(User).where(User.login == data["username"], User.password == data["password"])).scalars())
    return len(user_in_db) > 0


def check_for_completion(data):
    completion_in_db = list(db.session.execute(
        db.select(Completion).where(Completion.user_id == get_user_id_by_token(data["token"]),
                                    Completion.level == data["level"],
                                    Completion.difficulty == data["difficulty"])).scalars())

    return len(completion_in_db) > 0


def create_user(data):
    user_id = secrets.token_hex(TOKEN_HALF_LENGTH)
    db.session.execute(
        db.insert(User).values(id=user_id, login=data["username"], password=data["password"]))
    db.session.execute(
        db.insert(Settings).values(user_id=user_id, song_volume=100,
                                   sounds_volume=100,
                                   move_left='A',
                                   move_right='D',
                                   move_up='W',
                                   move_down='S',
                                   jump='Space',
                                   pause='esc',
                                   bg_enabled=1))
    db.session.commit()


def add_completion(data):
    if check_for_completion(data):
        db.session.execute(db.delete(Completion).where(Completion.user_id == get_user_id_by_token(data["token"]),
                                                       Completion.level == data["level"],
                                                       Completion.difficulty == data["difficulty"]))
    db.session.execute(
        db.insert(Completion).values(id=secrets.token_hex(TOKEN_HALF_LENGTH),
                                     user_id=get_user_id_by_token(data["token"]),
                                     level=data["level"], difficulty=data["difficulty"],
                                     stars=data["stars"], time=data["time"]))
    db.session.commit()


def change_settings(data):
    db.session.execute(
        db.update(Settings).where(Settings.user_id == get_user_id_by_token(data["token"])).values(
            song_volume=data["song_volume"],
            sounds_volume=data["sounds_volume"],
            move_left=data["move_left"],
            move_right=data["move_right"],
            move_up=data["move_up"],
            move_down=data["move_down"],
            jump=data["jump"],
            pause=data["pause"],
            bg_enabled=data["bg_enabled"]))

    db.session.commit()


def check_token(data):
    date = datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    date_values = list(map(int, date.split()))
    token_date = \
        list(
            db.session.execute(db.select(Token).where(Token.user_id == get_user_id_by_token(data["token"]))).scalars())[
            0][
            "date"]
    token_date_values = list(map(int, token_date.split()))

    date_in_sec = date_values[0] * SEC_IN["YEAR"] + date_values[1] * SEC_IN["MONTH"] + \
                  date_values[2] * SEC_IN["DAY"] + date_values[3] * SEC_IN["HOUR"] + \
                  date_values[4] * SEC_IN["MINUTE"] + date_values[5]

    token_date_in_sec = token_date_values[0] * SEC_IN["YEAR"] + token_date_values[1] * SEC_IN["MONTH"] + \
                        token_date_values[2] * SEC_IN["DAY"] + token_date_values[3] * SEC_IN["HOUR"] + \
                        token_date_values[4] * SEC_IN["MINUTE"] + token_date_values[5]

    if date_in_sec - token_date_in_sec > SEC_IN["MONTH"]:
        db.session.execute(db.delete(Token).where(Token.user_id == get_user_id_by_token(data["token"])))
        db.session.commit()
        return "expired"
    else:
        return "actual"


def get_settings(data):
    res = list(
        db.session.execute(
            db.select(Settings).where(Settings.user_id == get_user_id_by_token(data["token"]))).scalars())[0]
    return {"song_volume": res.song_volume, "sounds_volume": res.sounds_volume,
            "move_left": res.move_left, "move_right": res.move_right, "move_up": res.move_up,
            "move_down": res.move_down, "jump": res.jump, "pause": res.pause, "bg_enabled": res.bg_enabled}


def get_completions(data):
    if "username" not in data.keys():
        res = list(
            db.session.execute(
                db.select(Completion).where(Completion.user_id == get_user_id_by_token(data["token"]))).scalars())

    else:
        res = list(
            db.session.execute(
                db.select(Completion).where(
                    Completion.user_id == get_user_id_by_login(data["username"]))).scalars())
    ans = []
    for comp in res:
        ans.append({"level": comp.level, "difficulty": comp.difficulty, "stars": comp.stars, "time": comp.time})
    return ans
