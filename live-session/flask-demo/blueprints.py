from flask import Flask, Blueprint, render_template, request, make_response, jsonify

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)
students_bp = Blueprint('students', __name__, url_prefix='/students')

@main_bp.route('/')
def index():
    query_param = request.args.get('q')
    return render_template('index.html', query=query_param)

@main_bp.route('/<name>')
def show(name):
    user = {
        "name": name
    }

    return make_response(jsonify(user), 200)

@main_bp.route('/about')
def about():
    return f"This is the about page!"

@auth_bp.route('/login', methods=['POST'])
def login():
    names = [ 'frae', 'john', 'fi', 'sheryl', 'kim', 'miguel' ]
    name = request.json['name']

    if name in names:
        return make_response(f"{name} is logged in!", 200)

    return make_response(f"Unsuccessful!", 404)

# /students
@students_bp.route('/')
def show_students():
    return render_template('show_students.html', students=["frae", "kim", "fi", "sheryl", "miguel"])

@students_bp.route('/<string:name>')
def show_student(name):
    return f"The student is {name}!"

# /students/ - print all the students
# /students/:name - print the student