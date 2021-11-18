from query_builder import *
from access import *
import sys
import os

DATABASE = 'current'
TABLETEST = ';DROP %^t!)e@(s#*t$& WHERE \\'
TABLECONTROL = 'test'
def query_builder_test():
    # Tests for the query builder module
    a = queryBuilder(DATABASE, TABLETEST)
    b = queryBuilder(DATABASE, TABLECONTROL)
    assert a.create_table() == b.create_table()
    assert a.insert_into_table(3) == b.insert_into_table(3)
    assert a.select_from_table() == b.select_from_table()
    assert a.update_into_table() == b.update_into_table()
    assert a.delete_from_table() == b.delete_from_table()


PORTFOLIO_FIRST_ADD = ('AAPL', 27, 182.74)
PORTFOLIO_SECOND_ADD = ('FARM', 85, 13.94)
PORTFOLIO_THIRD_ADD = ('AAPL', 62, 39)
PORTFOLIO_FOURTH_ADD = ('BB', 1793265, 91830562.70916523)
def portfolio_access_testing():
    c = portfolioDB()
    c.setup_portfolio_table()
    c.add_to_portfolio_table(*PORTFOLIO_FIRST_ADD)
    c.add_to_portfolio_table(*PORTFOLIO_SECOND_ADD)
    c.add_to_portfolio_table(*PORTFOLIO_THIRD_ADD)
    c.add_to_portfolio_table(*PORTFOLIO_FOURTH_ADD)
    print('VIEWING TABLE BEFORE DELETION')
    c.see_portfolio_table()
    c.delete_from_portfolio_table('BB')
    print('VIEWING TABLE BEFORE DROP')
    c.see_portfolio_table()
    print(c.tables)
    c.drop_portfolio_table()
    print('DELETING TABLE NOW')
    c.see_portfolio_table()
    c.close_database()

WATCHLIST_FIRST_ADD = ('AAPL', 182.74)
WATCHLIST_SECOND_ADD = ('FARM', 13.94)
WATCHLIST_THIRD_ADD = ('AAPL', 39)
WATCHLIST_FOURTH_ADD = ('BB', 91830562.70916523)
def watchlist_access_testing():
    c = watchlistDB('want')
    c.setup_watchlist_table()
    c.add_to_watchlist_table(*WATCHLIST_FIRST_ADD)
    c.add_to_watchlist_table(*WATCHLIST_SECOND_ADD)
    c.add_to_watchlist_table(*WATCHLIST_THIRD_ADD)
    c.add_to_watchlist_table(*WATCHLIST_FOURTH_ADD)
    print('VIEWING TABLE BEFORE DELETION')
    c.see_watchlist_table()
    c.delete_from_watchlist_table('BB')
    print('VIEWING TABLE BEFORE DROP')
    c.see_watchlist_table()
    c.drop_watchlist_table()
    print('DELETING TABLE NOW')
    c.see_watchlist_table()
    c.close_database()
