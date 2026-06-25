from datetime import datetime, timezone


def time_ago(dt):
    """Return a human-friendly relative timestamp."""

    if dt is None:
        return "Unknown"

    # Ensure UTC-aware datetime
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)

    now = datetime.now(timezone.utc)
    seconds = int((now - dt).total_seconds())

    if seconds < 60:
        return f"{seconds} sec ago"

    minutes = seconds // 60
    if minutes < 60:
        return f"{minutes} min ago"

    hours = minutes // 60
    if hours < 24:
        return f"{hours} hr ago"

    days = hours // 24
    return f"{days} day{'s' if days != 1 else ''} ago"