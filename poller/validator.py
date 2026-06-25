from poller.models import BossLocation


def validate(location: BossLocation) -> BossLocation:
    """
    Validate collector output.

    Raises:
        ValueError if required fields are missing.
    """

    if not location.source:
        raise ValueError("Missing source")

    if not location.boss:
        raise ValueError("Missing boss")

    if not location.current_map:
        raise ValueError("Missing map")

    if location.confidence < 0 or location.confidence > 1:
        raise ValueError("Confidence must be between 0 and 1")

    return location