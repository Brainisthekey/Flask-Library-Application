from validate_data.filter_keywords import search_books_api, add_books_to_dictionary, sorting_a_single_book, sorting_value_if_list, sorting_ISBN
from unittest import mock
from data.test_data import response_google_api_book, return_value_api_book_total_items_0, sorted_params, return_from_add_books_to_dict, return_if_elements_in_list_int, return_if_elements_in_list_list, return_if_elements_in_list_none, return_if_elements_in_list_str, return_value_if_list, return_value_if_str, return_value_if_int, return_value_if_none, return_if_element_dict, return_value_if_dict, return_str_if_element_of_list_str, return_str, sorting_isbn, return_str_sorting_isbn



@mock.patch('validate_data.filter_keywords.requests.get')
def test_search_book_api(mock_request):
    mock_request.return_value = mock.Mock(
        **{'status_code': 200, 'json.return_value': response_google_api_book}
    )
    assert search_books_api(mode_of_sort='inauthor', keywords='flower') == response_google_api_book


@mock.patch('validate_data.filter_keywords.search_books_api')
@mock.patch('validate_data.filter_keywords.sorting_a_single_book')
def test_add_books_to_dictionary(mock_search_single_book, mock_search_api):

    mock_search_api.return_value = return_value_api_book_total_items_0
    assert add_books_to_dictionary(mode_of_sort='inauthor', keywords='flower') == None

    mock_search_api.return_value = response_google_api_book
    mock_search_single_book.return_value = sorted_params
    assert add_books_to_dictionary(mode_of_sort='inauthor', keywords='flower') == return_from_add_books_to_dict

@mock.patch('validate_data.filter_keywords.sorting_value_if_list')
def test_sorting_a_single_book(mock_sorting_if_list):
    
    mock_sorting_if_list.return_value = return_value_if_list
    assert sorting_a_single_book(params=return_if_elements_in_list_list) == [return_value_if_list]

    assert sorting_a_single_book(params=return_if_elements_in_list_str) == return_value_if_str

    assert sorting_a_single_book(params=return_if_elements_in_list_int) == return_value_if_int
    
    assert sorting_a_single_book(params=return_if_elements_in_list_none) == return_value_if_none


@mock.patch('validate_data.filter_keywords.sorting_ISBN')
def test_sorting_value_if_list(mock_sorting_isbn):

    mock_sorting_isbn.return_value = return_value_if_dict
    assert sorting_value_if_list(list_of_values=return_if_element_dict) == return_value_if_dict

    assert sorting_value_if_list(list_of_values=return_str_if_element_of_list_str) == return_str

def test_sorting_ISBN():

    assert sorting_ISBN(sorting_isbn) == return_str_sorting_isbn
