import sys

from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config, Config

# Extensions
db = SQLAlchemy()

# Celery client
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL, backend=Config.RESULT_BACKEND)


@celery.task
def test_task(arg):
    print("HELLO THERE!!!", file=sys.stderr)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(2.0, test_task.s(), name='Hello every 2 seconds')


def create_app(config_name):
    app = Flask(__name__)

    print(config_name + " configuration loaded", file=sys.stderr)

    # Initialise app configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialise extensions
    # SQLAlchemy
    db.init_app(app)

    # Celery
    celery.conf.update(app.config)

    # Module Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app
