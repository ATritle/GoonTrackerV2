from flask import Blueprint

from database.models import PollResult
from poller.poller import run_once

bp = Blueprint("main", __name__)


@bp.route("/")
def home():

    latest = (
        PollResult.query
        .order_by(PollResult.polled_at.desc())
        .first()
    )

    if latest is None:
        return "No data"

    return f"""
    <h1>GoonTracker V2</h1>

    <h2>{latest.boss}</h2>

    <h3>{latest.current_map}</h3>

    Confidence: {latest.confidence}
    """


@bp.route("/admin/poll")
def manual_poll():

    result = run_once()

    return {
        "source": result.source,
        "boss": result.boss,
        "map": result.current_map,
        "confidence": result.confidence,
    }