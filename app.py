import os

from flask import Flask

from config import Config
from database.db import db
from database.models import PollResult
from poller.poller import run_once
from poller.scheduler import PollScheduler
from web.routes import bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(bp)

with app.app_context():

    db.create_all()

    # Seed the database with an initial poll if empty
    if not PollResult.query.first():
        run_once()

# Start the background scheduler
scheduler = PollScheduler(interval=30)

# Prevent Flask debug mode from starting two scheduler threads
if os.environ.get("WERKZEUG_RUN_MAIN") == "true" or not app.debug:
    scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)