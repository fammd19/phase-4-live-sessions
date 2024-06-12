from flask import Blueprint, render_template, make_response, jsonify, request
#from users import users #commented out to get it from database
from models import db, User

user_bp = Blueprint("users", __name__, url_prefix="/users")

#as using user_bp will prepend with /users
@user_bp.route("/")
def index():
    users = User.query.all()

    new_users = []

    for user in users:
        new_users.append(user.to_json())
    return make_response(new_users, 200)

    #return render_template("users_index.html", users=users)

@user_bp.route("/", methods=["POST"])
def create():
    name = request.json["name"]
    sex = request.json["sex"]
    location = request.json["location"]

    new_user = User(name=name, sex=sex, location=location)
    db.session.add(new_user)
    db.session.commit()

    if new_user.id:
        return make_response(jsonify(new_user.to_json()), 201)


@user_bp.route("/<string:username>")
def show_user_by_username(username):
    user = User.query.filter(User.name.like(username)).first()

    if user:
        return render_template("show_user.html", user=user)

    return render_template("user_not_found.html")

    # user_found = None
    # for user in users:
    #     if username.lower() == user["name"]:
    #         user_found = user
    #         break

    # if user_found:
    #     return render_template("show_user.html", user=user_found)

    # return render_template("user_not_found.html")

@user_bp.route("/<int:user_id>")
def show_user_by_id(user_id):

    user = User.query.filter(User.id == user_id).first()
    
    if user:
        return make_response(jsonify(user.to_json()))
        #return render_template("show_user.html", user=user)

    return render_template("user_not_found.html")
    # for user in users:
    #     if user_id == user["id"]:
    #         return render_template("show_user.html", user=user)

    # return render_template("user_not_found.html")