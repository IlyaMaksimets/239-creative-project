from sqlalchemy.orm import Mapped, mapped_column
from .base import db


class Settings(db.Model):
    user_id: Mapped[str] = mapped_column(primary_key=True)
    song_volume: Mapped[int]
    sounds_volume: Mapped[int]
    move_left: Mapped[str]
    move_right: Mapped[str]
    move_up: Mapped[str]
    move_down: Mapped[str]
    jump: Mapped[str]
    pause: Mapped[str]
