from flask import Flask, Blueprint, render_template, make_response, jsonify

main_bp = Blueprint ("main", __name__)
auth_bp = Blueprint ("auth", __name__)
students_bp = Blueprint ("students", __name__, url_prefix="/students")


@main_bp.route("/")
def index():
    query_param = request.args.get("q")
    return render_template("index.html", query=query_param)


@main_bp.route("/<name>")
def show(name):
    user = {
        "name": name
    }

    return make_response(jsonify(user), 200)

#this the index of the students blue print
@students_bp.route("/")
def show_students():
    return render_template("show_students.html", students=["frae", "fi", "miguel", "sheryl", "kim"])

@students_bp.route("/<string:name>")
def show_student(name):
    return f"The student is {name}!"