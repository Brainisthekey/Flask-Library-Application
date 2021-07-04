from app import db


class Library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    authors = db.Column(db.String(250), nullable=False)
    publishedDate = db.Column(db.String(250), nullable=False)
    ISBN = db.Column(db.String(250), nullable=False)
    pagesCount = db.Column(db.String(250), nullable=False)
    previewLink = db.Column(db.String(250), nullable=False)
    languages = db.Column(db.String(250), nullable=False)

db.create_all()