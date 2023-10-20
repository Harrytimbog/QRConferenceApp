from .auth import auth_blueprint
from .conference import conference_blueprint

def register_blueprints(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(conference_blueprint)
