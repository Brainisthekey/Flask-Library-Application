from validate_data.search_in_liblary import formated_date, check_format_to_search
from data.test_data import string_to_test_fromated_date, return_list_of_str_date, test_formated_date_none, return_none, string_to_test_wrong_fromat, string_to_test_first_greater
from data.notification_message import eror_message_bad_format, error_message_first_greater
from unittest import mock




def test_formated_date():
    #
    assert formated_date(date=string_to_test_fromated_date) == return_list_of_str_date

    assert formated_date(date=test_formated_date_none) == return_none

    assert formated_date(date=string_to_test_wrong_fromat) == eror_message_bad_format

    assert formated_date(date=string_to_test_first_greater) == error_message_first_greater


@mock.patch('validate_data.search_in_liblary.formated_date')
@mock.patch('validate_data.search_in_liblary.search_in_year')
@mock.patch('validate_data.search_in_liblary.search_in_language')
@mock.patch('validate_data.search_in_liblary.search_in_author')
@mock.patch('validate_data.search_in_liblary.search_in_tittle')
def test_check_format_to_search(
                            mock_search_in_title,
                            mock_search_in_author,
                            mock_search_in_language,
                            mock_search_in_year,
                            mock_fromated_date

):
    return_value_object = 'database_object'
    mock_search_in_title.return_value = return_value_object
    mock_search_in_author.return_value = return_value_object
    mock_search_in_language.return_value = return_value_object
    mock_search_in_year.return_value = return_value_object

    mock_fromated_date.return_value = None
    assert check_format_to_search(
                        keyword='wrong_request',
                        search_by_title='',
                        search_by_authors='',
                        search_by_languages='',
                        search_by_date='wrong_request'
    ) == None

    mock_fromated_date.return_value = 'test'
    assert check_format_to_search(
                        keyword='good_format_date',
                        search_by_title='',
                        search_by_authors='',
                        search_by_languages='',
                        search_by_date='good_format_date'
    ) == return_value_object

    assert check_format_to_search(
                        keyword='test',
                        search_by_title='test',
                        search_by_authors='',
                        search_by_languages='',
                        search_by_date=''
    ) == return_value_object

    assert check_format_to_search(
                        keyword='test',
                        search_by_title='',
                        search_by_authors='test',
                        search_by_languages='',
                        search_by_date=''
    ) == return_value_object

    assert check_format_to_search(
                        keyword='test',
                        search_by_title='',
                        search_by_authors='',
                        search_by_languages='test',
                        search_by_date=''
    ) == return_value_object

    assert check_format_to_search(
                        keyword='test',
                        search_by_title='',
                        search_by_authors='',
                        search_by_languages='test',
                        search_by_date=''
    ) == return_value_object
