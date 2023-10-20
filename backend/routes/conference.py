from flask import Blueprint, request, jsonify, g
from extensions import db
from models import Conference, User
from functools import wraps


conference_blueprint = Blueprint("conferences", __name__)


# Create a decorator to ensure user ownership
def requires_ownership(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        conference = Conference.query.get_or_404(kwargs["id"])
        if g.user.id != conference.user_id and not g.user.is_admin:
            return jsonify({"message": "You don't have the permission."}), 403
        return f(*args, **kwargs)

    return decorated_function


@conference_blueprint.route("/conferences", methods=["POST"])
def create_conference():
    data = request.json
    new_conference = Conference(
        title=data["title"],
        description=data["description"],
        date_time=data["date_time"],
        venue=data["venue"],
        rsvp=data["rsvp"],
        image_url=data["image_url"],
        url=data["url"],
        user_id=data["user_id"],
    )
    db.session.add(new_conference)
    db.session.commit()
    return jsonify({"message": "Conference created successfully"}), 201


@conference_blueprint.route("/conferences", methods=["GET"])
def get_conferences():
    conferences = Conference.query.all()
    return jsonify([conference.serialize() for conference in conferences]), 200


@conference_blueprint.route("/conferences/<int:id>", methods=["GET"])
def get_conference(id):
    conference = Conference.query.get_or_404(id)
    return jsonify(conference.serialize()), 200


@conference_blueprint.route("/conferences/<int:id>", methods=["PUT"])
@requires_ownership
def update_conference(id):
    conference = Conference.query.get_or_404(id)
    data = request.json
    conference.title = data["title"]
    conference.description = data["description"]
    conference.date_time = data["date_time"]
    conference.venue = data["venue"]
    conference.rsvp = data["rsvp"]
    conference.image_url = data["image_url"]
    conference.url = data["url"]
    db.session.commit()
    return jsonify({"message": "Conference updated successfully"}), 200


@conference_blueprint.route("/conferences/<int:id>", methods=["DELETE"])
@requires_ownership
def delete_conference(id):
    conference = Conference.query.get_or_404(id)
    db.session.delete(conference)
    db.session.commit()
    return jsonify({"message": "Conference deleted successfully"}), 200
