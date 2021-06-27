import sqlite3

class Datalayer(object):
    _cursor = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Datalayer, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.conn = sqlite3.connect('db/database.db')
        self.conn.row_factory = sqlite3.Row

a = Datalayer()
b = Datalayer()
print(a.conn is b.conn)


