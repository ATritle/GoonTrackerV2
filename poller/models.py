from dataclasses import dataclass
from datetime import datetime


@dataclass
class BossLocation:

    source: str
    boss: str
    current_map: str
    confidence: float
    polled_at: datetime

    game_mode: str | None = None
    reporter: str | None = None
    report_time: str | None = None