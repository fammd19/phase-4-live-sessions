from flask import Flask, render_template
from flask_migrate import Migrate
from user_bp import user_bp
from book_bp import book_bp
from models import db

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(book_bp)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=3000, debug=True)