from config import db, bcrypt
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    isAdmin = db.Column(db.Integer, default=0)
    #set name to start with a _ because we want to make it private/ encapsulated
    _hashed_password = db.Column(db.String)

    @hybrid_property
    def hashed_password (self):
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, password):
        hashed_password=bcrypt.generate_password_hash(password.encode('utf-8'))

        self._hashed_password = hashed_password.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._hashed_password, password.encode('utf-8'))

    def __repr__(self):
        return f"<User {self.id}: {self.username}>"

    
