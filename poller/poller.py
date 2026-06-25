import logging

from .collectors.dummy import DummyCollector
from .validator import validate
from .storage import save

logger = logging.getLogger(__name__)

def run_once():

    collector = DummyCollector()

    location = collector.poll()

    validated = validate(location)

    save(validated)

    logger.info(
        "Collector %s reported %s on %s",
        validated.source,
        validated.boss,
        validated.current_map,
    )

    return validated