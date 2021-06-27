from datetime import time
from genericpath import exists
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from validate_data.check_and_filter_requestform import check_type_and_create_list_of_books, check_requests_form
from validate_data.search_in_liblary import check_format_to_search
from db.db_commands import get_book, get_all_books_from_liblary, add_new_book_to_liblary, insert_books_from_GoogleBooks_into_database, edit_book_by_id, delete_book_by_id, delete_all_books
import os
from db.init_db import initialization_database

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/', methods=('GET', 'POST'))
def index():
    """Main page"""
    Libraries = get_all_books_from_liblary()
    return render_template('index.html', Libraries=Libraries)

#Вот тут добавить валидацию на вызов пустых строк
@app.route('/create', methods=('GET', 'POST'))
def create():
    """Page to create a new book"""
    if request.method == 'POST':
        title = request.form['title']
        authors = request.form['authors']
        publishedDate = request.form['publishedDate']
        ISBN = request.form['ISBN']
        pagesCount = request.form['pagesCount']
        previewLink = request.form['previewLink']
        languages = request.form['languages']

        if not all((title, authors, publishedDate, ISBN, pagesCount, previewLink, languages)):
            flash('All fields must be filled!')
        else:
            add_new_book_to_liblary(title, authors, publishedDate, ISBN, pagesCount, previewLink, languages)
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/search', methods=('GET', 'POST'))
def search():
    """Search in GoogleBooks liblary"""
    if request.method == 'POST':
        title = request.form['title']
        authors = request.form['authors']
        publisher = request.form['publisher']
        subject = request.form['subject']
        isbn = request.form['isbn']
        lccn = request.form['lccn']
        oclc = request.form['oclc']

        keyword_to_search = check_requests_form([title, authors, publisher, subject, isbn, lccn, oclc])
        if keyword_to_search is None:
            flash("You can use only 1 parametr to search")
            return redirect(url_for('search'))
        list_of_books = check_type_and_create_list_of_books(
                                                    params_to_search=keyword_to_search,
                                                    title=title,
                                                    authors=authors,
                                                    publisher=publisher,
                                                    subject=subject,
                                                    isbn=isbn,
                                                    lccn=lccn,
                                                    oclc=oclc
                                                    )
        if list_of_books is None:
            flash("I didn't find anything for you request. Please, try again")
            return redirect(url_for('search'))
        else:
            insert_books_from_GoogleBooks_into_database(list_of_books)
        return redirect(url_for('index'))
    return render_template('search.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    """Edit books"""
    book = get_book(id)
    if request.method == 'POST':
        title = request.form['title']
        authors = request.form['authors']
        publishedDate = request.form['publishedDate']
        ISBN = request.form['ISBN']
        pagesCount = request.form['pagesCount']
        previewLink = request.form['previewLink']
        languages = request.form['languages']
        #Вот здесь нужно добавить валидацию питоновским кодом, проверки данных
        #Валидация должна быть такая же как и при добавлении новой книги
        #Тоесть код может постариться
        if not all((title, authors, publishedDate, ISBN, pagesCount, previewLink, languages)):
            flash('All fields must be filled!')
        else:
            edit_book_by_id(title, authors, publishedDate, ISBN, pagesCount, previewLink, languages, id)
            return redirect(url_for('index'))

    return render_template('edit.html', book=book)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    """Delete book from database"""
    book = delete_book_by_id(id)
    flash('"{}" was successfully deleted!'.format(book['title']))
    return redirect(url_for('index'))

#Узнать функция долждна называться так же как и путь,
#Наверно нет, но попробывать стоит
@app.route('/delete_all', methods=('POST', 'GET'))
def delete_all():
    """Delete all books from the database"""
    delete_all_books()
    flash('All books was successfully deleted!')
    return redirect(url_for('index'))


@app.route('/search_in', methods=('POST', 'GET'))
def search_in():
    """Search book in created liblary"""
    if request.method == 'POST':
        search_by_title = request.form['search_by_title']
        search_by_authors = request.form['search_by_authors']
        search_by_languages = request.form['search_by_languages']
        search_by_date = request.form['search_by_date']

        keyword_to_search = check_requests_form([search_by_title, search_by_authors, search_by_languages, search_by_date])
        if keyword_to_search is None:
            flash("You can use only 1 parametr to search")
            return redirect(url_for('search_in'))
        else:
            book = check_format_to_search(
                                    keyword=keyword_to_search,
                                    search_by_title=search_by_title,
                                    search_by_authors=search_by_authors,
                                    search_by_languages=search_by_languages,
                                    search_by_date=search_by_date
                                    )
            if book is None:
                flash("Please write date in correct form: start_year-end_year. Example: 1990-2020")
                return redirect(url_for('search_in'))
            elif book == []:
                flash("I didn't find anything for you'r request, try again")
                return redirect(url_for('search_in'))
        return render_template('search_in.html', Libraries=book)
    return render_template('search_in.html')

if __name__ == '__main__':
    if os.path.exists('db/database.db'):
        app.run()
    else:
        initialization_database()
        app.run()
