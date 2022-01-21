from flask import Flask

from quant.rest import trade
from quant.rest import hello
from quant.extensions import db, migrate


def create_app():
    app = Flask('app')
    configure_app(app)
    configure_db(app)
    configure_extensions(app, False)
    register_blueprints(app)

    return app


def configure_app(app):
    # default configuration
    app.config.from_object("quant.config")



def configure_db(app):
    try:
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://{username}:{password}@{host}:{port}/{dbname}?client_encoding=utf8".\
            format(username=app.config.get("USERNAME"), password=app.config.get("PASSWORD"),
                   host=app.config.get("HOST"),port=app.config.get("PORT"),dbname=app.config.get("DBNAME"))
    except Exception as e:
        print(e)
    return app


def configure_extensions(app, cli):
    db.init_app(app)


def register_blueprints(app):
    app.register_blueprint(trade.blueprint)
    app.register_blueprint(hello.blueprint)