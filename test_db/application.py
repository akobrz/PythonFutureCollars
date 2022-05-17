import flask
import flask_sqlalchemy

config = {
    "DEBUG": True,
    "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
    "SQLALCHEMY_TRACK_MODIFICATIONS": True
}

app = flask.Flask(__name__)
app.config.from_mapping(config)
db = flask_sqlalchemy.SQLAlchemy(app)



