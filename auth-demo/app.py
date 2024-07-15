from flask import make_response, session, request
from flask_cors import CORS
from config import app, api
from models import db, User
from flask_restful import Resource

@app.route('/')
def index():
    return make_response({"message":"Welcome!"}, 200)

@app.before_request
def authenticate():
    #exempted_endpoints = ['signup', 'login']
    exempted_routes = {
        "/":["GET"],
        "/signup":["POST"],
        "/login":["POST"]
    }

    if request.path in exempted_routes:
        allowed_methods = exempted_routes[request.path]
        if request.method in allowed_methods:
            return None
    
    if 'user' not in session:
        return make_response({"error":"Unauthorised"}, 403)

    # if 'user' not in session and request.endpoint not in exempted_endpoints:
    #     return make_response({"error":"Unauthorised"}, 403)

    #hashed out is an alternative version which doesn't include checking the methods of the routes


class Signup(Resource):
    def post(self):
        user = User(username=request.json.get('username'), isAdmin=request.json.get('isAdmin'), hashed_password = request.json.get('password'))

        db.session.add(user)
        db.session.commit()

        if user.id:
            session['user'] = user.to_dict()

            return make_response({"message":"User account created..."}, 201)

        else:
            return make_response({"error":"Unsuccessful"}, 400)
        
class Login(Resource):
    def post(self):
        user = User.query.filter(User.username == request.json.get('username')).first()

        if user and user.authenticate(request.json.get('password')):
            session['user'] = user.to_dict()

            return make_response({"message": "Login successful..."}, 200)

        else:
            return make_response ({"error":"Unathorised..."}, 403)

class Logout(Resource):
    def delete(self):
        session.pop('user', None)

        return make_response({"message":"Logout successful..."}, 200)

class Me(Resource):
    def get(self):
        if 'user' in session:
            return make_response(session['user'], 200)

        else:
            return make_response({"error":"No user"}, 403)

class Users(Resource):
    def get(self):

        user = session['user']

        if user['isAdmin'] ==1:
            users = [ user.to_dict() for user in User.query.all() ]

            return make_response(users, 200)

        else:
            return make_response({"error":"No admin access"}, 403)


api.add_resource(Signup, '/signup', endpoint="signup")
api.add_resource(Login, '/login', endpoint="login")
api.add_resource(Logout, '/logout', endpoint="logout")
api.add_resource(Me, '/me', endpoint="me")
api.add_resource(Users, '/users', endpoint="users")


CORS(app)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
