
from flask import Flask, make_response, request
from flask_restful import Resource, Api
from flask_migrate import Migrate
from models import User, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return make_response({"message":"API working..."}, 200)

#for /users
class Users(Resource):
    def get(self):
        users = [ user.to_dict() for user in User.query.all() ]
        return make_response(users, 200)

    def post(self):
        new_user = User(username=request.json.get('username'), location=request.json.get('location'), email=request.json.get('email'), age=request.json.get('age'))
        db.session.add(new_user)
        db.session.commit()

        return make_response(new_user.to_dict(), 201)

class UserByID(Resource):
    def get(self, id):
        user = User.query.filter(User.id==id).first()
        if user:
            return make_response(user.to_dict(), 200)
        else:
            return make_response({"error":"User not found"}, 403)

    def patch(self, id):
        user = User.query.filter(User.id==id).first()
        if user:
            for attr in request.json:
                setattr(user, attr, request.json[attr])

            db.session.commit()

            return make_response(user.to_dict(), 200)
        
        else:
            return make_response({"error":"User not found"}, 403)


    def delete(self, id):
        user = User.query.filter(User.id==id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response({"message":"Delete successful"}, 200)

api = Api(app)

api.add_resource(Users, '/users')
api.add_resource(UserByID, '/users/<int:id>')

if __name__ == "__main__":
    app.run(port=4000, debug=True)