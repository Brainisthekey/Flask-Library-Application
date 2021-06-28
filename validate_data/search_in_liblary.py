from typing import List, Optional
from db.db_commands import (
    search_in_author,
    search_in_tittle,
    search_in_language,
    search_in_year,
)
from data.notification_message import (
    eror_message_bad_format,
    error_message_first_greater,
)


def formated_date(date) -> List:
    """
    Filter string and return errors if occured

    if length string is not equal 2:
        return errors message
    if string date is not a numeric:
        return errors message
    if first year greater than the second:
        return error message
    Return:
        List[int, int]
    """
    if "-" in date:
        date_splited = date.split("-")
        if len(date_splited) != 2:
            return eror_message_bad_format
        filtered_data = list(filter(lambda x: x.isnumeric() or x == "0", date_splited))
        if len(filtered_data) == len(date_splited):
            if int(filtered_data[0]) > int(filtered_data[1]):
                return error_message_first_greater
            return [int(year) for year in filtered_data]
    else:
        return None


def check_format_to_search(
    keyword, search_by_title, search_by_authors, search_by_languages, search_by_date
):
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
        range_date = formated_date(date=search_by_date)
        if range_date == eror_message_bad_format:
            return eror_message_bad_format
        elif range_date == error_message_first_greater:
            return error_message_first_greater
        elif range_date == None:
            return None
        return search_in_year(range_date)
