from database.db import db
from database.models import PollResult


def save(location):

    row = PollResult(
        source=location.source,
        boss=location.boss,
        current_map=location.current_map,
        confidence=location.confidence,
        polled_at=location.polled_at,
    )

    db.session.add(row)
    db.session.commit()

    return row