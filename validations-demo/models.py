from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from flask import make_response
import re

db = SQLAlchemy()

class User (db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, unique=True)
    location = db.Column(db.String, default="Australia")
    email = db.Column(db.String)
    age = db.Column(db.Integer)

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError("Username is a required field")

        return username

    @validates('location')
    def validate_location(self, key, location):
        locations = ["australia","nz"]

        if location.lower() not in locations:
            raise ValueError("Location must be Australia or NZ")

        return location

    @validates('email')
    def validate_username(self, key, email):
        if User.query.filter(User.email == email).first():
            raise ValueError("Email already taken")

        if not re.match(r'^[A-Za-z0-9]+@[A-Za-z0-9.]+\.[A-Za-z]{2,7}$', email):
            raise ValueError("Email not valid")

        return email

    @validates('age')
    def validate_username(self, key, age):
        if not isinstance(age, (int,)):
            raise ValueError("Age must be an integer")

        if age < 18 or age > 70:
            raise ValueError("Age must be between 18 and 70")

        return age


    def __repr__(self):
        return f"<User {self.id}: {self.username}"

    
