import os
import sys
import sqlite3
from .query_builder import queryBuilder

class dbAccess():
    """The parent class for all database operations.
    This class contains standard methods for all databases"""

    def __init__(self, nickname):
        # The portfolio database will always be named the same
        self.portfolio_db = 'portfolio.db'
        # Need to support multiple watchlist databases so the '%n' can be replaced with an arbitrary string
        self.watchlist_db = 'watchlist.db'
        self.nickname = nickname
        # A tuple is recomended as passing it in prevents SQL injection attacks
        self.nickname_tuple = (self.nickname,)

    def create_database_connection(self, database_name):
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        return connection, cursor

class portfolioDB(dbAccess):
    """A child class of dbAccess that interacts with the portfolio stock holdings database."""
    def __init__(self, nickname='test'):
        # Import parent class attributes
        dbAccess.__init__(self, nickname)
        self.qb = queryBuilder('portfolio', nickname)
        # Create a connection and a cursor object for the watchlist database
        self.conn, self.c = self.create_database_connection(self.portfolio_db)
        self.tables = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

    def setup_portfolio_table(self):
        """Sets up a database for portfolio stock holdings."""
        query = self.qb.create_table()
        self.conn.execute(query)
        self.conn.commit()

    def add_to_portfolio_table(self, ticker, quantity, basis_price):
        "Adds or edits a portfolio table in the database."
        query = self.qb.select_from_table()
        result = self.c.execute(query, (ticker,)).fetchall()
        exists_binary = len(result)
        if exists_binary == 1:
            old_quantity = result[0][2]
            old_basis_price = result[0][3]
            new_quantity = old_quantity + quantity
            adjusted_basis_price = (old_basis_price * (old_quantity / new_quantity)) + (basis_price * (quantity / new_quantity))
            update_values = (new_quantity, adjusted_basis_price, ticker)
            query = self.qb.update_into_table()
            self.c.execute(query, update_values)
        else:
            self.length = self.c.execute(self.qb.total_rows_from_table()).fetchall()[0][0]
            id = self.length + 1
            insert = (id, ticker, quantity, basis_price)
            query = self.qb.insert_into_table(4)
            self.conn.execute(query, insert)
        self.conn.commit()

    def drop_portfolio_table(self):
        """Deletes a portfolio table from the database."""
        query = self.qb.drop_table()
        self.conn.execute(query)
        self.conn.commit()

    def delete_from_portfolio_table(self, ticker):
        """Deletes a row from the portfolio table specified."""
        query = self.qb.delete_from_table()
        self.conn.execute(query, (ticker,))
        self.conn.commit()

    def see_portfolio_table(self):
        query = self.qb.all_rows_in_table()
        for row in self.conn.execute(query):
            print(row)

    def close_database(self):
        self.c.close()
        self.conn.close()
        pass


class watchlistDB(dbAccess):
    """A child class of dbAccess that interacts with the portfolio stock holdings database."""
    def __init__(self, nickname='test'):
        # Import parent class attributes
        dbAccess.__init__(self, nickname)
        self.qb = queryBuilder('watchlist', nickname)
        # Create a connection and a cursor object for the watchlist database
        self.conn, self.c = self.create_database_connection(self.watchlist_db)
        self.tables = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

    def setup_watchlist_table(self):
        """Sets up a database for watchlist stock holdings."""
        query = self.qb.create_table()
        self.conn.execute(query)
        self.conn.commit()

    def add_to_watchlist_table(self, ticker, price):
        query = self.qb.select_from_table()
        result = self.c.execute(query, (ticker,)).fetchall()
        exists_binary = len(result)
        if exists_binary == 1:
            print("This ticker already exists in the watchlist!")
            return
        self.length = self.c.execute(self.qb.total_rows_from_table()).fetchall()[0][0]
        id = self.length + 1
        insert = (id, ticker, price)
        query = self.qb.insert_into_table(3)
        self.c.execute(query, insert)
        self.conn.commit()

    def drop_watchlist_table(self):
        """Deletes a watchlist table from the database."""
        query = self.qb.drop_table()
        self.conn.execute(query)
        self.conn.commit()

    def delete_from_watchlist_table(self, ticker):
        """Deletes a row from the watchlist table specified."""
        query = self.qb.delete_from_table()
        self.conn.execute(query, (ticker,))
        self.conn.commit()

    def see_watchlist_table(self):
        query = self.qb.all_rows_in_table()
        for row in self.c.execute(query):
            print(row)

    def close_database(self):
        self.c.close()
        self.conn.close()
        pass
