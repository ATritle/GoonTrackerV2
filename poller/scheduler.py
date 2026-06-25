import logging
import threading
import time

from poller.poller import run_once

logger = logging.getLogger(__name__)


class PollScheduler:

    def __init__(self, interval=30):
        self.interval = interval
        self.thread = None
        self.running = False

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._loop,
            daemon=True,
        )

        self.thread.start()

        logger.info("Poll scheduler started")

    def stop(self):
        self.running = False

    def _loop(self):

        while self.running:

            try:
                run_once()

            except Exception:
                logger.exception("Polling failed")

            time.sleep(self.interval)