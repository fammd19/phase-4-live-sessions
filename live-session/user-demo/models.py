from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User (db.Model): #User is a subclass of db.model

    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False) #constraint of 200 characters
    sex = db.Column(db.String)
    location = db.Column(db.String)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "sex": self.sex,
            "location": self.location
        }

    def __repr__(self):
        return f"<{self.id}: {self.name}>" #angled brackets are just a display preference, not needed

    
class Book (db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False) 
    genre = db.Column(db.String)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre
        }

    def __repr__(self):
        return f"<Book: {self.title}>"