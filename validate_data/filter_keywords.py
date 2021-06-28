import requests

base_path = 'https://www.googleapis.com/books/v1/volumes?q='

def search_books_api(mode_of_sort: str, keywords) -> dict:
    """
    Request to the GoogleBooksApi

    Parametrs:
        mode_of_sort: str
        Special mode to sort my search

        keywords: str
        Special character for search
    Return:
        Response json object
    """
    response = requests.get(base_path + f'{mode_of_sort}:{keywords}')
    return response.json()

def add_books_to_dictionary(mode_of_sort: str, keywords) -> list:
    """
    Sorting JSON object

    Parametrs:
        mode_of_sort: str
        Special mode to sort my search

        keywords: str
        Special character for search
    Return:
        List of sorted books
    """
    list_to_return = []
    result_dict = {}
    result_of_sorting = search_books_api(mode_of_sort=mode_of_sort, keywords=keywords)
    if result_of_sorting['totalItems'] == 0:
        return None
    for book in result_of_sorting['items']:
        result_dict[book['volumeInfo']['title']] = {
            'title' : book['volumeInfo'].get('title', None),
            'authors' : book['volumeInfo'].get('authors', None),
            'publishedDate' : book['volumeInfo'].get('publishedDate', None),
            'ISBN' : book['volumeInfo'].get('industryIdentifiers', None),
            'pagesCount' : book['volumeInfo'].get('pageCount', None),
            'previewLink' : book['volumeInfo'].get('previewLink', None),
            'languages' : book['volumeInfo'].get('language', None)
            }
    for params in result_dict.values():
        sorted_params = sorting_a_single_book(params=params)
        list_to_return.append(sorted_params)
    return list_to_return
    
def sorting_a_single_book(params: dict) -> list:
    """
    Validate params in a single book

    Parametrs:
        params: dict
        Book values
    Return:
        List of sorted parametrs of book
    """
    result_to_return = []
    for value in params.values():
        if value == None:
            result_to_return.append('None')
        elif isinstance(value, int):
            result_to_return.append(str(value))
        elif isinstance(value, str):
            result_of_check = check_string_if_date(value)
            result_to_return.append(result_of_check)
        elif isinstance(value, list):
            result_to_return.append(sorting_value_if_list(list_of_values=value))
    return result_to_return

def check_string_if_date(date_string: str) -> int:
    if date_string.find('-') != -1:
        string_joined = ''.join(x for x in date_string[:4] if x.isnumeric() or x == '0')
        if len(string_joined) == len(date_string[:4]):
            return int(string_joined)
        else:
            return date_string
    return date_string



def sorting_value_if_list(list_of_values: list) -> str:
    """
    Soring list of values

    Parametrs:
        list_of_values: list
        filter list object
    Return:
        Sorted params
    """
    list_of_strings = []
    for element in list_of_values:
        if isinstance(element, str):
            return element
        if isinstance(element, dict):
            list_of_strings.append(''.join(sorting_ISBN(dict_of_elements=element)))
    return ' and '.join(x for x in list_of_strings)

def sorting_ISBN(dict_of_elements: dict) -> str:
    """Sort the dictionary to become a string"""
    return ' : '.join(value for value in dict_of_elements.values())
