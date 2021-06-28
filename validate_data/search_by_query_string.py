from db.db_commands import search_in_tittle, search_in_author, search_in_language, search_in_year

example_string_title = '?title=Jack London'
example_string_author = '?author=Earle Labor'
example_string_laguage = '?language=un'
example_string_date = '?date=2010-2020'


def search_in_query_title(title):
    return search_in_tittle(title)
def search_in_query_author(author):
    return search_in_author(author)
def search_in_query_language(language):
    return search_in_language(language)
def search_in_query_date(date):
    return search_in_year(date)
