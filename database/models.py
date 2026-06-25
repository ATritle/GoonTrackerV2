from datetime import datetime
from .db import db


class PollResult(db.Model):
    __tablename__ = "poll_results"

    id = db.Column(db.Integer, primary_key=True)

    source = db.Column(db.String(50), nullable=False)

    boss = db.Column(db.String(50), nullable=False)

    current_map = db.Column(db.String(50), nullable=False)

    confidence = db.Column(db.Float, nullable=False)

    game_mode = db.Column(db.String(10))
    reporter = db.Column(db.String(100))
    report_time = db.Column(db.String(50))

    polled_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(datetime.UTC),
        nullable=False
    )
