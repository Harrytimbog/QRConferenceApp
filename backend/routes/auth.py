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


@auth_blueprint.route("/test", methods=["GET"])
def test():
    return "Test successful!", 200
