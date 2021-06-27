import sqlite3
from db.db_commands import search_in_author, search_in_tittle, search_in_language, search_in_year


def formated_date(date) -> list:
    """Filter string"""
    if '-' in date:
        return date.split('-')
    else:
        return None


def check_format_to_search(keyword, search_by_title, search_by_authors, search_by_languages, search_by_date):
    """
    Soring list of values

    Parametrs:
        list_of_values: list
        filter list object
    Return:
        Sorted params
    
    """
    if keyword in search_by_title:
        return search_in_tittle(search_by_title)
    if keyword in search_by_authors:
        return search_in_author(search_by_authors)
    if keyword in search_by_languages:
        return search_in_language(search_by_languages)
    if keyword in search_by_date:
        range_date = formated_date(search_by_date)
        if range_date is not None:
            return search_in_year(range_date)
        return None




#print(formated_date('1990-2020'))
#print(search_in_year(date=['1990', '2020']))