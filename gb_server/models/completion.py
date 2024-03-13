from sqlalchemy.orm import Mapped, mapped_column
from .base import db


class Completion(db.Model):
    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str]
    level: Mapped[int]
    difficulty: Mapped[int]
    stars: Mapped[int]
    time: Mapped[str]
