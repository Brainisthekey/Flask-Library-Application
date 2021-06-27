import sqlite3



def initialization_database():
    connection = sqlite3.connect('db/database.db')
    with open('db/schema.sql') as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    cur.execute("INSERT INTO Libraries (title, authors, publishedDate, ISBN, pagesCount, previewLink, languages) VALUES (?, ?, ?, ?, ?, ?, ?)",
                ('Hobbit czyli Tam i z powrotem',
                'J. R. R. Tolkien',
                '2004',
                '8320717507',
                '315',
                'http://books.google.pl/books?id=YyXoAAAACAAJ&dq=Hobbit&hl=&cd=1&source=gbs_api',
                'un'
    ))
    cur.execute("INSERT INTO Libraries (title, authors, publishedDate, ISBN, pagesCount, previewLink, languages) VALUES (?, ?, ?, ?, ?, ?, ?)",
                ('Balanda',
                'Tolkien',
                '2003',
                '8320717501',
                '500',
                'http://books.google.pl/books?id=DqLPAAAAMAAJ&q=Hobbit&dq=Hobbit&hl=&cd=4&source=gbs_api',
                'en'
    ))
    connection.commit()
    connection.close()