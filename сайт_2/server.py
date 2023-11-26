from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ABOBA.db"
db = SQLAlchemy(app)

class Gotov(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class ReseptGotov(db.Model):
    genre_id = db.Column(db.Integer, db.ForeignKey("gotov.id"), nullable=False, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("resept.id"), nullable=False, primary_key=True)

class Resept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String, nullable=False, default="")
    image_url = db.Column(db.String,nullable=False)
    genres = db.relationship('Gotov', secondary=ReseptGotov.__table__, lazy='subquery',
        backref=db.backref('resepts', lazy=True))


@app.route("/")
def index():
    genres = Gotov.query.all()
    movies = Resept.query.all()
    return render_template("index.html", genres=genres, movies=movies)

if __name__ == '__main__':
    app.run(debug=True)