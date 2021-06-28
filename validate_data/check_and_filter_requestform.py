from validate_data.filter_keywords import add_books_to_dictionary


def check_requests_form(filed_of_request: list) -> str:
    """Check request.form:
    If only one field was completed -> return keyword_string,
    If more than one -> return None
    """
    not_empty_field = list(filter(lambda x: len(x), filed_of_request))
    if len(not_empty_field) == 1:
        return validate_string(not_empty_field[0])
    else:
        return None


def iter_in_tuple_of_string(tuple_string: tuple) -> bool:
    """Return True if elements of tuple is not an empy strings else False"""
    return len(list(filter(lambda x: validate_string(x), tuple_string))) == len(tuple_string)


def validate_string(string_to_validate: str) -> str:
    """Return string if is not empty"""
    return None if string_to_validate.isspace() else string_to_validate


def check_type_and_create_list_of_books(
    params_to_search: str,
    title: str,
    authors: str,
    publisher: str,
    subject: str,
    isbn: str,
    lccn: str,
    oclc: str,
) -> list:
    """Returning list of book filtered by keyword"""
    if params_to_search in title:
        list_of_books = add_books_to_dictionary(mode_of_sort="intitle", keywords=title)
    elif params_to_search in authors:
        list_of_books = add_books_to_dictionary(
            mode_of_sort="inauthor", keywords=authors
        )
    elif params_to_search in publisher:
        list_of_books = add_books_to_dictionary(
            mode_of_sort="inpublisher", keywords=publisher
        )
    elif params_to_search in subject:
        list_of_books = add_books_to_dictionary(
            mode_of_sort="subject", keywords=subject
        )
    elif params_to_search in isbn:
        list_of_books = add_books_to_dictionary(
            mode_of_sort="isbn", keywords=isbn
        )
    elif params_to_search in lccn:
        list_of_books = add_books_to_dictionary(
            mode_of_sort="lccn", keywords=lccn
        )
    elif params_to_search in oclc:
        list_of_books = add_books_to_dictionary(
            mode_of_sort="oclc", keywords=oclc
        )
    else:
        return None
    return list_of_books
