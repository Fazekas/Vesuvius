from flask import Flask
from src.controllers.card_controller import card_blueprint
from src.dbms.rdb import db
from src.schemas.marshmallow import ma


# Runs flask app factory
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('development.cfg')
    else:
        app.config.from_mapping(test_config)

    # Init db
    db.init_app(app)

    # Init ma
    ma.init_app(app)

    app.register_blueprint(card_blueprint)

    @app.cli.command('create-all')
    def create_all():
        db.create_all(app=app)

    @app.cli.command('drop-all')
    def drop_all():
        db.drop_all(app=app)

    return app
