import sqlite3

class dbAccess():
    def __init__(self, database):
        self.database = database
        self.current_database = 'current.db'
        self.watchlist_database = 'watchlist.db'
