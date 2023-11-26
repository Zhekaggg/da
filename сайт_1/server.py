from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class GenreMovie(db.Model):
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False, primary_key=True)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=1)
    created_date = db.Column(db.Date,nullable=False, default=datetime.strptime("1973-09-17","%Y-%m-%d"))
    description = db.Column(db.String, nullable=False, default="")
    image_url = db.Column(db.String,nullable=False)
    genres = db.relationship('Genre', secondary=GenreMovie.__table__, lazy='subquery',
        backref=db.backref('movies', lazy=True))
    




  
@app.route("/")
def index():
    genres = Genre.query.all()
    movies = Movie.query.all()
    return render_template("index.html", genres=genres, movies=movies)




if __name__ == '__main__':
    app.run(debug=True)