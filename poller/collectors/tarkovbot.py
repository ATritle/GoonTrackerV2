import requests
from bs4 import BeautifulSoup

from poller.models import BossLocation

from datetime import datetime, UTC


class TarkovBotCollector:
    URL = "https://tarkovbot.eu/goonstracker"

    def poll(self):

        response = requests.get(self.URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        report = soup.select_one(".latest-report.pvp-report")

        if report is None:
            raise RuntimeError("Could not find latest PvP report")

        map_text = report.select_one(".report_map").get_text(strip=True)

        game_mode = None

        if "(PVP)" in map_text:
            game_mode = "PVP"
            current_map = map_text.replace("(PVP)", "").strip()

        elif "(PVE)" in map_text:
            game_mode = "PVE"
            current_map = map_text.replace("(PVE)", "").strip()

        else:
            current_map = map_text

        report_time = report.select_one(".report_time").get_text(strip=True)

        reporter = report.select_one(".reportedby").get_text(strip=True)

        # Remove the "Reported by" prefix
        reporter = reporter.removeprefix("Reported by").strip()

        return BossLocation(
            source="TarkovBot",
            boss="Goons",
            current_map=current_map,
            confidence=0.95,
            polled_at=datetime.now(UTC),
            game_mode=game_mode,
            reporter=reporter,
            report_time=report_time,
        )