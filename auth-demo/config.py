from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_bcrypt import Bcrypt




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK MODIFICATION'] = False
#for secret key, use encryption or similar, not like the below
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy()

db.init_app(app)

migrate = Migrate(app, db)

api=Api(app)

bcrypt = Bcrypt()


