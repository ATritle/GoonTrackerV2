from .db import db


class Spawn(db.Model):
    __tablename__ = "spawns"

    id = db.Column(db.Integer, primary_key=True)

    map_name = db.Column(db.String(50), nullable=False)

    boss_name = db.Column(db.String(50), nullable=False)

    reported_at = db.Column(db.DateTime)

    confidence = db.Column(db.Float)