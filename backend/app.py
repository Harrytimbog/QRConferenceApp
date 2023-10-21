from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from extensions import db
from routes import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///qrconferenceapp.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "some-secret-key"
    CORS(app, origins=["http://localhost:3000"])
    # CORS(app)

    register_blueprints(app)
    db.init_app(app)
    Migrate(app, db)

    # from routes.auth import auth_blueprint
    # from routes.conference import conference_blueprint

    # app.register_blueprint(auth_blueprint)
    # app.register_blueprint(conference_blueprint)

    return app


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
