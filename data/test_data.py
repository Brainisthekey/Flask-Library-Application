
response_google_api_book = {
  "kind": "books#volumes",
  "totalItems": 200,
  "items": [
        {
        "volumeInfo": {
            "title": "Rose Book",
            "authors": ["Aoyama Flower Market"],
            "publishedDate": "2009-05",
            "industryIdentifiers": [
            {
                "type": "ISBN_10",
                "identifier": "4891947950"
            },
            {
                "type": "ISBN_13",
                "identifier": "9784891947958"
            }
            ],
            "pageCount": 94,
            "language": "un",
            "previewLink": "http://books.google.pl/books?id=X_-6PgAACAAJ&dq=inauthor:flower&hl=&cd=1&source=gbs_api"
        }}]
}

sorted_dict_with_books = {'title': 'Rose Book', 'authors': ['Aoyama Flower Market'], 'publishedDate': '2009-05', 'ISBN' : [{'type': 'ISBN_10', 'identifier': '4891947950'}, {'type': 'ISBN_13', 'identifier': '9784891947958'}], 'pagesCount': 94, 'previewLink': 'http://books.google.pl/books?id=X_-6PgAACAAJ&dq=inauthor:flower&hl=&cd=1&source=gbs_api', 'languages': 'un'}
sorted_params = ['Rose Book', 'Aoyama Flower Market', '2009-05', 'ISBN_10 : 4891947950 and ISBN_13 : 9784891947958', '94', 'http://books.google.pl/books?id=X_-6PgAACAAJ&dq=inauthor:flower&hl=&cd=1&source=gbs_api', 'un']
return_value_api_book_total_items_0 = {'totalItems': 0}
return_from_add_books_to_dict = [['Rose Book', 'Aoyama Flower Market', '2009-05', 'ISBN_10 : 4891947950 and ISBN_13 : 9784891947958', '94', 'http://books.google.pl/books?id=X_-6PgAACAAJ&dq=inauthor:flower&hl=&cd=1&source=gbs_api', 'un']]


return_if_elements_in_list_str = {1: 'test', 2: 'test', 3: 'test'}
return_value_if_str = ['test', 'test', 'test']

return_if_elements_in_list_none = {1: None, 2: None, 3: None}
return_value_if_none = ['None', 'None', 'None']

return_if_elements_in_list_int = {'book1': 1, 'book2': 2, 'book3' : 3}
return_value_if_int = ['1', '2', '3']

return_if_elements_in_list_list = {1: ['test']}
return_value_if_list = 'test'

return_if_element_dict = [{'type': 'ISBN_10', 'identifier': '4891947950'}]
return_value_if_dict = 'ISBN_10 : 4891947950'

return_str_if_element_of_list_str = ['test']
return_str = 'test'

sorting_isbn = {'type': 'ISBN_10', 'identifier': '4891947950'}
return_str_sorting_isbn = 'ISBN_10 : 4891947950'

string_to_test_fromated_date = '1990-2020'
return_list_of_str_date = [1990, 2020]

test_formated_date_none = '77777'
return_none = None

data_for_check_length_one = ['', 'test', '']
data_for_check_length_two = ['test', 'test']

validate_string_with_only_spaces = '  '
valid_string = ' t e s t '

example_good_tuple = (1, 2, 3)
example_bad_tuple = (1, 2)
