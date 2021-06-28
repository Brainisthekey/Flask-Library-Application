from db.db_commands import search_in_tittle, search_in_author, search_in_language, search_in_year
from validate_data.search_in_liblary import formated_date
from data.notification_message import eror_message_bad_format, error_message_first_greater



def search_in_query_title(title):
    return search_in_tittle(title)
def search_in_query_author(author):
    return search_in_author(author)
def search_in_query_language(language):
    return search_in_language(language)
def search_in_query_date(date):
    range_date = formated_date(date=date)
    if range_date == eror_message_bad_format:
        return eror_message_bad_format
    elif range_date == error_message_first_greater:
        return error_message_first_greater
    elif range_date == None:
        return None
    else:
        return search_in_year(range_date)

    #What if return like that
    #return eror_message_bad_format if range_date == 1 else 2
