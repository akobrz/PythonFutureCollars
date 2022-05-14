import flask
import flask_alembic
import flask_sqlalchemy

config = {
    "DEBUG": True,
    "SQLALCHEMY_DATABASE_URI": "sqlite:///..\\database\\hunter.db",
    "SQLALCHEMY_TRACK_MODIFICATIONS": True
}

app = flask.Flask(__name__)
app.config.from_mapping(config)
db = flask_sqlalchemy.SQLAlchemy(app)
alembic = flask_alembic.Alembic()

if __name__ == "__main__":
    alembic.init_app(app)
    pass