import os
import sys
import sqlite3

class dbAccess():
    """The parent class for all database operations.
    This class contains standard methods for all databases"""

    def __init__(self):
        # The current database will always be named the same
        self.current_db = 'current.db'
        # Need to support multiple watchlist databases so the '%n' can be replaced with an arbitrary string
        self.watchlist_db_base = '%nwatchlist.db'


class currentDB(dbAccess):
    """A child class of dbAccess that interacts with the current stock holdings database."""
    def __init__(self):
        # Import parent class attributes
        dbAccess.__init__(self)
        # Create a connection with the database
        self.conn = sqlite3.connect(self.current_db)
        # Create a cursor object
        self.c = self.conn.cursor()

    def _setup_current_db(self):
        """Sets up a database for current stock holdings.
        Only to be used on a fresh current file!"""
        self.conn.execute("""CREATE TABLE current
        (ID INT PRIMARY KEY  NOT NULL,
        TICKER TEXT NOT NULL,
        PRICE REAL NOT NULL);
        """)

    def add_to_current_db(self, id, ticker, price):
        insert = (id, ticker, price)
        self.c.execute(f"INSERT INTO current VALUES (?,?,?)", insert);
        self.conn.commit()

    def see_current_db(self):
        for row in self.c.execute('SELECT * FROM current'):
            print(row)


class watchlistDB(dbAccess):
    """A child class of dbAccess that interacts with the current stock holdings database."""
    def __init__(self, nickname):
        # Import parent class attributes
        dbAccess.__init__(self)
        self.nickname = nickname
        self.watchlist_db = nickname + self.watchlist_db_base
        # Create a connection with the database
        self.conn = sqlite3.connect(self.watchlist_db)
        # Create a cursor object
        self.c = self.conn.cursor()
        # A tuple is recomended as passing it in prevents SQL injection attacks
        self.nickname_tuple = (self.nickname,)

    def _setup_watchlist_db(self):
        """Sets up a database for current stock holdings.
        Only to be used on a fresh current file!"""
        self.conn.execute("""CREATE TABLE ?
        (ID INT PRIMARY KEY  NOT NULL,
        TICKER TEXT NOT NULL,
        PRICE REAL NOT NULL);
        """, self.nickname_tuple)

    def add_to_watchlist_db(self, id, ticker, price):
        insert = (id, ticker, price)
        self.c.execute(f"INSERT INTO current VALUES (?,?,?)", insert);
        self.conn.commit()

    def see_watchlist_db(self):
        for row in self.c.execute('SELECT * FROM ?', self.nickname_tuple):
            print(row)
