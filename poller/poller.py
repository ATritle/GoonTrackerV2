from database.db import db
from database.models import PollResult

from .collectors.dummy import DummyCollector


def run_once():

    collector = DummyCollector()

    data = collector.poll()

    row = PollResult(
        source=data.source,
        boss=data.boss,
        current_map=data.current_map,
        confidence=data.confidence,
        polled_at=data.polled_at,
    )

    db.session.add(row)

    db.session.commit()

    return row
