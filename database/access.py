import os
import sys
import sqlite3

class dbAccess():
    """The parent function for all database operations."""
    def __init__(self):
        # The current database will always be named the same
        self.current_db = 'current.db'
        # Need to support multiple watchlist databases so the '%n' can be replaced with an arbitrary string
        self.watchlist_db_base = '%nwatchlist.db'

    def _setup_current_db(self):
        already_exists = os.path.isfile(self.current_db)
        conn = sqlite3.connect(self.current_db)
        conn.execute("""CREATE TABLE current
        (ID INT PRIMARY KEY  NOT NULL,
        TICKER TEXT NOT NULL,
        PRICE REAL NOT NULL);
        """)

    def add_to_current_db(self, id, ticker, price):
        conn = sqlite3.connect(self.current_db)
        c = conn.cursor()
        insert = (id, ticker, price)
        c.execute(f"INSERT INTO current VALUES (?,?,?)", insert);
        conn.commit()

    def see_current_db(self):
        conn = sqlite3.connect(self.current_db)
        c = conn.cursor()
        for row in c.execute('SELECT * FROM current'):
            print(row)

    def _setup_watchlist_db(self):
        pass

d = dbAccess()
# d._setup_current_db()
# d.add_to_current_db(3,'FARM',150)
d.see_current_db()
