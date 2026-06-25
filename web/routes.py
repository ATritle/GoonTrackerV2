from flask import Blueprint, render_template, jsonify

from database.models import PollResult
from poller.poller import run_once
from web.utils import time_ago

bp = Blueprint("main", __name__)


@bp.route("/")
def home():

    latest = (
        PollResult.query
        .order_by(PollResult.polled_at.desc())
        .first()
    )

    return render_template(
        "index.html",
        latest=latest,
        last_updated=time_ago(latest.polled_at),
    )


@bp.route("/admin/poll")
def manual_poll():

    result = run_once()

    return {
        "source": result.source,
        "boss": result.boss,
        "map": result.current_map,
        "confidence": result.confidence,
    }

@bp.route("/api/latest")
def api_latest():

    latest = (
        PollResult.query
        .order_by(PollResult.polled_at.desc())
        .first()
    )

    return jsonify(
        {
            "boss": latest.boss,
            "map": latest.current_map,
            "game_mode": latest.game_mode,
            "reporter": latest.reporter,
            "source": latest.source,
            "confidence": latest.confidence,
            "report_time": latest.report_time,
            "last_updated": time_ago(latest.polled_at),
        }
    )