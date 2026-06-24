from datetime import datetime
from .db import db


class PollResult(db.Model):
    __tablename__ = "poll_results"

    id = db.Column(db.Integer, primary_key=True)

    source = db.Column(db.String(50), nullable=False)

    boss = db.Column(db.String(50), nullable=False)

    current_map = db.Column(db.String(50), nullable=False)

    confidence = db.Column(db.Float, nullable=False)

    polled_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )
