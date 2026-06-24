from poller.poller import run_once
from flask import Flask

from config import Config
from database.db import db
from web.routes import bp
from database.models import PollResult

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(bp)

with app.app_context():
    db.create_all()


with app.app_context():

    db.create_all()

    if not PollResult.query.first():
        run_once()

if __name__ == "__main__":
    app.run(debug=True)
