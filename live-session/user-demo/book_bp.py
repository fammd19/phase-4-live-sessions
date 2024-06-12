from flask import Blueprint, render_template, make_response, jsonify, request
from models import db, Book

book_bp = Blueprint("books", __name__, url_prefix="/books")

@book_bp.route("/")
def index():
    books = Book.query.all()

    books_list = []

    for book in books:
        books_list.append(book.to_json())

    return make_response(jsonify(books_list), 200)

@book_bp.route("/", methods=["POST"])
def create():
    title = request.json["title"]
    genre = request.json["genre"]

    new_book = Book(title=title, genre=genre)
    db.session.add(new_book)
    db.session.commit()

    if new_book.id:
        return make_response(jsonify(new_book.to_json()))