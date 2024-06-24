from flask_restful import Resource
from models import db, Book
from flask import make_response, request

class Books(Resource):

    def get(self):
        books = [ book.to_dict() for book in Book.query.all() ]

        return make_response(books, 200)

    def post(self):
        new_book = Book(title=request.json['title'], genre=request.json['genre'])
        db.session.add(new_book)
        db.session.commit()

        if new_book.id:
            return make_response(new_book.to_dict(), 201)

        else:
            ({"error":"create unsuccessful"}, 403)


class BookById(Resource):

    def get(self, id):
        book = Book.query.filter(Book.id == id).first()

        if book:
            return make_response(book.to_dict(), 200)

        else:
            return make_response({"error":"No book found"}, 404)






