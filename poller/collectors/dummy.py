from datetime import datetime

from poller.collector import Collector
from poller.models import BossLocation


class DummyCollector(Collector):

    def poll(self):

        return BossLocation(
            source="Dummy",
            boss="Goons",
            current_map="Customs",
            confidence=1.0,
            polled_at=datetime.utcnow()
        )
