from dataclasses import dataclass
from datetime import datetime


@dataclass
class BossLocation:

    source: str

    boss: str

    current_map: str

    confidence: float

    polled_at: datetime