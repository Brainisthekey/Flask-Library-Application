import sqlite3
from werkzeug.exceptions import abort

class Datalayer(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Datalayer, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.conn = sqlite3.connect('db/database.db')
        self.conn.row_factory = sqlite3.Row

def get_book(book_id):
    """Check if book exist in database"""
    conn = Datalayer().conn
    book = conn.execute('SELECT * FROM Libraries WHERE id = ?',
                        (book_id,)).fetchone()
    conn.close()
    if book is None:
        abort(404)
    return book

def get_all_books_from_liblary():
    """Get all books"""
    conn = Datalayer().conn
    Libraries = conn.execute('SELECT * FROM Libraries').fetchall()
    conn.close()
    return Libraries

def add_new_book_to_liblary(
                        title: str,
                        authors: str,
                        publishedDate: int,
                        ISBN: str,
                        pagesCount: str,
                        previewLink: str,
                        languages: str
):
    """Add new book"""
    conn = Datalayer().conn
    conn.execute("INSERT INTO Libraries (title, authors, publishedDate, ISBN, pagesCount, previewLink, languages) VALUES (?, ?, ?, ?, ?, ?, ?)",
    (title, authors, publishedDate, ISBN, pagesCount, previewLink, languages))
    conn.commit()
    conn.close()
    return 201

def insert_books_from_GoogleBooks_into_database(list_of_books: list):
    """Add books to the database from GoogleBooksApi"""
    conn = Datalayer().conn
    for number_of_book in range(len(list_of_books)):
        conn.execute("INSERT INTO Libraries (title, authors, publishedDate, ISBN, pagesCount, previewLink, languages) VALUES (?, ?, ?, ?, ?, ?, ?)",
        list_of_books[number_of_book])
        conn.commit()
    conn.close()
    return 200

def edit_book_by_id(
                title: str,
                authors: str,
                publishedDate: str,
                ISBN: str,
                pagesCount: str,
                previewLink: str,
                languages: str,
                id
):
    """Edit book in lablary"""
    conn = Datalayer().conn
    conn.execute('UPDATE Libraries SET title = ?, authors = ?, publishedDate = ?, ISBN = ?, pagesCount = ?, previewLink = ?, languages = ?'
    ' WHERE id = ?', (title, authors, publishedDate, ISBN, pagesCount, previewLink, languages, id))
    conn.commit()
    conn.close()
    return 200

def delete_book_by_id(id):
    """Delete book by id"""
    book = get_book(id)
    conn = Datalayer().conn
    conn.execute('DELETE FROM Libraries WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return book

def delete_all_books():
    """Delete all books from the database"""
    conn = Datalayer().conn
    conn.execute('DELETE FROM Libraries')
    conn.commit()
    conn.close()
    return 200

def search_in_tittle(title: str):
    conn = Datalayer().conn
    #Ахуел максиммально изза того, что параметры title должен быть написан именно (title,)
    book = conn.execute('SELECT * FROM Libraries WHERE title = ?', (title,)).fetchall()
    conn.close()
    return book

def search_in_author(author: str):
    conn = Datalayer().conn
    book = conn.execute('SELECT * FROM Libraries WHERE authors = ?', (author,)).fetchall()
    conn.close()
    return book

def search_in_language(language: str):
    conn = Datalayer().conn
    book = conn.execute('SELECT * FROM Libraries WHERE languages = ?', (language,)).fetchall()
    conn.close()
    return book

def search_in_year(date: list):
    conn = Datalayer().conn
    book = conn.execute('SELECT * FROM Libraries WHERE publishedDate BETWEEN ? AND ?', (date)).fetchall()
    conn.close()
    return book



