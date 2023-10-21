from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User

import bcrypt


auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/signup", methods=["POST"])
def signup():
    print("Request got here")
    data = request.get_json()
    hashed_password = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
    print("Request also got here")
    new_user = User(
        email=data["email"], password=hashed_password, full_name=data["full_name"]
    )
    print("Request got here also")
    db.session.add(new_user)
    db.session.commit()
    print("Request got here at last")

    return jsonify({"message": "User registered successfully!"}), 201


# More routes and functions for login, profile etc...


@auth_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()

    if user and bcrypt.checkpw(data["password"].encode("utf-8"), user.password):
        # Store the user's id in the session
        session["user_id"] = user.id
        return jsonify({"message": "Logged in successfully!"}), 200
    else:
        return jsonify({"message": "Invalid email or password!"}), 401


@auth_blueprint.route("/logout", methods=["POST"])
def logout():
    # Remove user_id from session
    session.pop("user_id", None)
    return jsonify({"message": "Logged out successfully!"}), 200


@auth_blueprint.route("/profile", methods=["GET"])
def profile():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"message": "User not logged in!"}), 401

    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found!"}), 404

    # Assuming your User model has attributes: email, full_name.
    # You can add more attributes if needed.
    user_data = {"email": user.email, "full_name": user.full_name}

    return jsonify(user_data), 200


@auth_blueprint.route("/test", methods=["GET"])
def test():
    return "Test successful!", 200
