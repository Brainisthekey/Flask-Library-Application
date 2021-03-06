from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, flash, redirect
from validate_data.check_and_filter_requestform import (
    check_type_and_create_list_of_books,
    check_requests_form,
    iter_in_tuple_of_string,
)
from data.notification_message import (
    error_message_first_greater,
    eror_message_bad_format,
    error_wrong_input_format,
    message_none_result,
    error_message_count_params,
    message_all_fields,
    notification_delete_all,
    message_only_spaces,
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "your secret key"

db = SQLAlchemy(app)

@app.route("/", methods=("GET", "POST"))
def index():
    from database.db_command_alch import get_all_book
    """Main page"""
    Libraries = get_all_book()
    return render_template("index.html", Libraries=Libraries)


@app.route("/create", methods=("GET", "POST"))
def create():
    from database.db_command_alch import add_new_book_to_liblary
    """Page to create a new book"""
    if request.method == "POST":
        title = request.form["title"]
        authors = request.form["authors"]
        publishedDate = request.form["publishedDate"]
        ISBN = request.form["ISBN"]
        pagesCount = request.form["pagesCount"]
        previewLink = request.form["previewLink"]
        languages = request.form["languages"]

        tuple_with_request_form = (
            title,
            authors,
            publishedDate,
            ISBN,
            pagesCount,
            previewLink,
            languages,
        )
        if not all(tuple_with_request_form):
            flash(message_all_fields)
        elif not iter_in_tuple_of_string(tuple_with_request_form):
            flash(message_only_spaces)
        else:
            add_new_book_to_liblary(
                title, authors, publishedDate, ISBN, pagesCount, previewLink, languages
            )
            return redirect(url_for("index"))
    return render_template("create.html")


@app.route("/search", methods=("GET", "POST"))
def search():
    from database.db_command_alch import insert_books_from_GoogleBooks_into_database
    """Search in GoogleBooks liblary"""
    if request.method == "POST":
        title = request.form["title"]
        authors = request.form["authors"]
        publisher = request.form["publisher"]
        subject = request.form["subject"]
        isbn = request.form["isbn"]
        lccn = request.form["lccn"]
        oclc = request.form["oclc"]

        keyword_to_search = check_requests_form(
            [title, authors, publisher, subject, isbn, lccn, oclc]
        )
        if keyword_to_search is None:
            flash(error_message_count_params)
            return redirect(url_for("search"))
        list_of_books = check_type_and_create_list_of_books(
            params_to_search=keyword_to_search,
            title=title,
            authors=authors,
            publisher=publisher,
            subject=subject,
            isbn=isbn,
            lccn=lccn,
            oclc=oclc,
        )
        if list_of_books is None:
            flash(message_none_result)
            return redirect(url_for("search"))
        else:
            insert_books_from_GoogleBooks_into_database(list_of_books)
        return redirect(url_for("index"))
    return render_template("search.html")


@app.route("/<int:id>/edit", methods=("GET", "POST"))
def edit(id):
    """Edit books"""
    from database.db_command_alch import get_book, edit_book_by_id
    book = get_book(id)
    if request.method == "POST":
        title = request.form["title"]
        authors = request.form["authors"]
        publishedDate = request.form["publishedDate"]
        ISBN = request.form["ISBN"]
        pagesCount = request.form["pagesCount"]
        previewLink = request.form["previewLink"]
        languages = request.form["languages"]

        if not all(
            (title, authors, publishedDate, ISBN, pagesCount, previewLink, languages)
        ):
            flash(message_all_fields)
        else:
            edit_book_by_id(
                title,
                authors,
                publishedDate,
                ISBN,
                pagesCount,
                previewLink,
                languages,
                id,
            )
            return redirect(url_for("index"))

    return render_template("edit.html", book=book)


@app.route("/<int:id>/delete", methods=("POST",))
def delete(id):
    from database.db_command_alch import delete_book_by_id
    """Delete book from database"""
    book = delete_book_by_id(id)
    flash('"{}" was successfully deleted!'.format(book))
    return redirect(url_for("index"))


@app.route("/delete_all", methods=("POST", "GET"))
def delete_all():
    from database.db_command_alch import delete_all_books
    """Delete all books from the database"""
    delete_all_books()
    flash(notification_delete_all)
    return redirect(url_for("index"))


@app.route("/search_in", methods=("POST", "GET"))
def search_in():
    from validate_data.search_in_liblary import check_format_to_search
    """Search book in created liblary"""
    if request.method == "POST":
        search_by_title = request.form["search_by_title"]
        search_by_authors = request.form["search_by_authors"]
        search_by_languages = request.form["search_by_languages"]
        search_by_date = request.form["search_by_date"]

        keyword_to_search = check_requests_form(
            [search_by_title, search_by_authors, search_by_languages, search_by_date]
        )
        if keyword_to_search is None:
            flash(error_message_count_params)
            return redirect(url_for("search_in"))
        else:
            book = check_format_to_search(
                keyword=keyword_to_search,
                search_by_title=search_by_title,
                search_by_authors=search_by_authors,
                search_by_languages=search_by_languages,
                search_by_date=search_by_date,
            )
            if book is None:
                flash(error_wrong_input_format)
                return redirect(url_for("search_in"))
            elif book == eror_message_bad_format:
                flash(eror_message_bad_format)
                return redirect(url_for("search_in"))
            elif book == error_message_first_greater:
                flash(error_message_first_greater)
                return redirect(url_for("search_in"))
            elif book == []:
                flash(message_none_result)
                return redirect(url_for("search_in"))
        return render_template("search_in.html", Libraries=book)
    return render_template("search_in.html")


@app.route("/books", methods=("GET", "POST"))
def search_by_query_string():
    from validate_data.search_by_query_string import (
    search_in_query_title,
    search_in_query_author,
    search_in_query_language,
    search_in_query_date,
    )
    """Search by query string"""
    request_title = request.args.get("title")
    request_author = request.args.get("author")
    request_language = request.args.get("language")
    request_date = request.args.get("date")

    if request_title:
        books = search_in_query_title(title=request_title)
    elif request_author:
        books = search_in_query_author(author=request_author)
    elif request_language:
        books = search_in_query_language(language=request_language)
    elif request_date:
        books = search_in_query_date(date=request_date)
        if books is None:
            flash(error_wrong_input_format)
            return redirect(url_for("search_by_query_string"))
        elif books == eror_message_bad_format:
            flash(eror_message_bad_format)
            return redirect(url_for("search_by_query_string"))
        elif books == error_message_first_greater:
            flash(error_message_first_greater)
            return redirect(url_for("search_by_query_string"))
        elif books == []:
            flash(message_none_result)
            return redirect(url_for("search_by_query_string"))
    else:
        return render_template("search_by_query.html")
    return render_template("search_by_query.html", Libraries=books)


if __name__ == "__main__":
    app.run(debug=True)
