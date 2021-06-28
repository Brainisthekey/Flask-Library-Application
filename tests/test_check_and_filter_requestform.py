from validate_data.check_and_filter_requestform import check_requests_form, validate_string, check_type_and_create_list_of_books, iter_in_tuple_of_string
from data.test_data import data_for_check_length_one, data_for_check_length_two, validate_string_with_only_spaces, valid_string, example_good_tuple, example_bad_tuple
from unittest import mock

@mock.patch('validate_data.check_and_filter_requestform.validate_string')
def test_check_requests_form(mock_validate_string):

    mock_validate_string.return_value = 'test'
    #data_for_check_length_one = ['', 'test', '']
    assert check_requests_form(filed_of_request=data_for_check_length_one) == 'test'
    #data_for_check_length_two = ['test', 'test']
    assert check_requests_form(filed_of_request=data_for_check_length_two) == None

@mock.patch('validate_data.check_and_filter_requestform.filter')
def test_iter_in_tuple_of_string(mock_filter):

    mock_filter.return_value = example_good_tuple
    #example_good_tuple = (1, 2, 3)
    assert iter_in_tuple_of_string(example_good_tuple) == True

    mock_filter.return_value = example_bad_tuple
    #exaple_good_tuple = (1, 2)
    assert iter_in_tuple_of_string(example_good_tuple) == False


def test_validate_string():

    #validate_string_with_only_spaces = '  '
    assert validate_string(string_to_validate=validate_string_with_only_spaces) == None
    #valid_string = ' t e s t '
    assert validate_string(string_to_validate=valid_string) == ' t e s t '



@mock.patch('validate_data.check_and_filter_requestform.add_books_to_dictionary')
def test_check_type_and_create_list_of_books(mock_add_book):

    mock_add_book.return_value = 'test'
    assert check_type_and_create_list_of_books(
                                params_to_search='test',
                                title='test',
                                authors='',
                                publisher='',
                                subject='',
                                isbn='',
                                lccn='',
                                oclc=''
    ) == 'test'

    assert check_type_and_create_list_of_books(
                                params_to_search='test',
                                title='',
                                authors='',
                                publisher='',
                                subject='',
                                isbn='',
                                lccn='',
                                oclc=''
    ) == None

    assert check_type_and_create_list_of_books(
                                params_to_search='test',
                                title='',
                                authors='test',
                                publisher='',
                                subject='',
                                isbn='',
                                lccn='',
                                oclc=''
    ) == 'test'
    assert check_type_and_create_list_of_books(
                                params_to_search='test',
                                title='',
                                authors='',
                                publisher='test',
                                subject='',
                                isbn='',
                                lccn='',
                                oclc=''
    ) == 'test'
    assert check_type_and_create_list_of_books(
                                params_to_search='test',
                                title='',
                                authors='',
                                publisher='',
                                subject='test',
                                isbn='',
                                lccn='',
                                oclc=''
    ) == 'test'

    assert check_type_and_create_list_of_books(
                                params_to_search='test',
                                title='',
                                authors='',
                                publisher='',
                                subject='test',
                                isbn='test',
                                lccn='',
                                oclc=''
    ) == 'test'

    assert check_type_and_create_list_of_books(
                                params_to_search='test',
                                title='',
                                authors='',
                                publisher='',
                                subject='',
                                isbn='',
                                lccn='test',
                                oclc=''
    ) == 'test'

    assert check_type_and_create_list_of_books(
                                params_to_search='test',
                                title='',
                                authors='',
                                publisher='',
                                subject='',
                                isbn='',
                                lccn='',
                                oclc='test'
    ) == 'test'



