from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db, Book
from flask_restful import Api
from controllers.books_controller import Books, BookById

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

migrate = Migrate(app, db)

api = Api(app)

db.init_app(app)

@app.route('/')
def index():
    return make_response( jsonify( { "message": "Welcome to the Book App!" } ), 200)

api.add_resource(Books, '/books')
api.add_resource(BookById, '/books/<int:id>')

if __name__ == "__main__":
    app.run(port=4000, debug=True)