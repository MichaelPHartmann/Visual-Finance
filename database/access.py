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
        self.watchlist_db = '%nwatchlist.db'

    def create_database_connection(self, database_name):
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        return connection, cursor

class currentDB(dbAccess):
    """A child class of dbAccess that interacts with the current stock holdings database."""
    def __init__(self):
        # Import parent class attributes
        dbAccess.__init__(self)
        # Create a connection and a cursor object for the watchlist database
        self.conn, self.c = self.create_database_connection(self.current_db)

        self.length = self.c.execute("SELECT COUNT(*) FROM current").fetchall()[0][0]


    def _setup_current_db(self):
        """Sets up a database for current stock holdings.
        Only to be used on a fresh current file!"""
        self.conn.execute("""
        CREATE TABLE current
        (ID INT PRIMARY KEY  NOT NULL,
        TICKER TEXT UNIQUE NOT NULL,
        QUANTITY INT NOT NULL,
        BASIS_PRICE REAL NOT NULL);
        """)


    def add_to_current_db(self, ticker, quantity, basis_price):
        result = self.c.execute("SELECT * FROM current WHERE TICKER = ?", (ticker,)).fetchall()
        exists_binary = len(result)
        if exists_binary == 1:
            old_quantity = result[0][2]
            old_basis_price = result[0][3]
            new_quantity = old_quantity + quantity
            adjusted_basis_price = (old_basis_price * (old_quantity / new_quantity)) + (basis_price * (quantity / new_quantity))
            update_values = (new_quantity, adjusted_basis_price, ticker)
            self.c.execute("UPDATE current SET QUANTITY = ?, BASIS_PRICE = ? WHERE TICKER = ?", update_values)
        else:
            id = self.length + 1
            insert = (id, ticker, quantity, basis_price)
            self.c.execute(f"INSERT INTO current VALUES (?,?,?,?);", insert)
        self.conn.commit()

    def see_current_db(self):
        for row in self.c.execute("""SELECT * FROM current"""):
            print(row)


class watchlistDB(dbAccess):
    """A child class of dbAccess that interacts with the current stock holdings database."""
    def __init__(self, nickname):
        # Import parent class attributes
        dbAccess.__init__(self)
        self.nickname = nickname
        # A tuple is recomended as passing it in prevents SQL injection attacks
        self.nickname_tuple = (self.nickname,)
        # Create a connection and a cursor object for the watchlist database
        self.conn, self.c = self.create_database_connection(self.watchlist_db)


    def _setup_watchlist_db(self):
        """Sets up a database for a stock watchlist."""
        self.conn.execute(f"""CREATE TABLE ?
        (ID INT PRIMARY KEY  NOT NULL,
        TICKER TEXT UNIQUE NOT NULL,
        PRICE REAL);
        """, self.nickname_tuple)

    def add_to_watchlist_db(self, ticker):
        result = self.c.execute("SELECT * FROM ? WHERE TICKER = ?", (self.nickname, ticker)).fetchall()
        exists_binary = len(result)
        assert exists_binary == 1, 'You already have the ticker in this watchlist'

        id = self.length + 1
        insert = (id, ticker)
        self.c.execute(f"INSERT INTO current VALUES (?,?);", insert)
        self.conn.commit()

    def see_watchlist_db(self):
        for row in self.c.execute('SELECT * FROM ?', self.nickname_tuple):
            print(row)


d = currentDB()
# d._setup_current_db()
d.add_to_current_db('AAPL',10,105)
d.add_to_current_db('FARM',35,18)
d.add_to_current_db('BB',20,7.50)
d.add_to_current_db('CLOV',4,25)
d.add_to_current_db('CCL',93,22.50)
d.add_to_current_db('DDL',93,22.50)
d.add_to_current_db('KHVD',645,76.78)

d.see_current_db()
