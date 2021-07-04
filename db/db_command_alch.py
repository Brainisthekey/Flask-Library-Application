from flask.helpers import flash
from sqlalchemy.orm import session
from database.init_db_alch import Library
from app import db
from flask import abort



def add_book_to_library():
    
    first_book = Library(
                title='Babasa',
                authors='authors',
                publishedDate='publishedDate',
                ISBN='ISBN',
                pagesCount='pagesCount',
                previewLink='previewLink',
                languages='languages'
                )
    check_exist = bool(db.session.query(Library).filter_by(dict(first_book)).first())
    if check_exist is False:
        db.session.add(first_book)
        db.session.commit()
    else:
        flash("The book is alredy exist")
        

def get_book(book_id):
    """Check if book exist in database"""
    book = db.session.query(Library).get(book_id)
    if book is None:
        abort(404)
    return book

def get_all_books_from_liblary():
    """Get all books"""
    return db.session.query(Library).all()

def add_new_book_to_liblary(
    title: str,
    authors: str,
    publishedDate: int,
    ISBN: str,
    pagesCount: str,
    previewLink: str,
    languages: str,
):
    """Add new book"""
    book = Library(
        title=title,
        authors=authors,
        publishedDate=publishedDate,
        ISBN=ISBN,
        pagesCount=pagesCount,
        previewLink=previewLink,
        languages=languages
    )
    check_exist = bool(db.session.query(Library).filter_by(title=title).first())
    if check_exist is False:
        db.session.add(book)
        db.session.commit()
    else:
        flash(f"The book {book.title} is alredy exist")
    return 201

def insert_books_from_GoogleBooks_into_database(list_of_books: list):
    """Add books to the database from GoogleBooksApi"""
    list_with_params = ['title', 'authors', 'publishedDate', 'ISBN', 'pagesCount', 'previewLink', 'languages']
    for one_book in list_of_books:
        dict_params = {list_with_params[i] : one_book[i] for i in range(len(list_with_params))}
        new_book_from_Google_Books = Library(**dict_params)
        check_exist = bool(db.session.query(Library).filter_by(title=dict_params['title']).first())
        if check_exist is False:
            db.session.add(new_book_from_Google_Books)
        else:
            flash(f"The book - {dict_params['title']} is alredy exist")
    db.session.commit()
    return 200

def edit_book_by_id(
    title: str,
    authors: str,
    publishedDate: str,
    ISBN: str,
    pagesCount: str,
    previewLink: str,
    languages: str,
    id,
):
    """Edit book in lablary"""
    db.session.query(Library).filter_by(id=id).update(dict(
        title=title,
        authors=authors,
        publishedDate=publishedDate,
        ISBN=ISBN,
        pagesCount=pagesCount,
        previewLink=previewLink,
        languages=languages
    ))
    db.session.commit()

def delete_book_by_id(id):
    """Delete book by id"""
    book = db.session.query(Library).get(id)
    title_of_book = book.title
    print(title_of_book)
    book = db.session.query(Library).filter_by(id=id).delete()
    db.session.commit()
    return title_of_book

def delete_all_books():
    """Delete all books from the database"""
    db.session.query(Library).delete()
    db.session.commit()

    
def search_in_tittle(title: str):
    return db.session.query(Library).filter_by(title=title).all()


def search_in_author(author: str):
    return db.session.query(Library).filter_by(authors=author).all()

def search_in_language(language: str):
    return db.session.query(Library).filter_by(languages=language).all()

def search_in_year(date: list):
    return db.session.query(Library).filter(Library.publishedDate.between(*date)).all()


def get_all_book():
    return db.session.query(Library).all()