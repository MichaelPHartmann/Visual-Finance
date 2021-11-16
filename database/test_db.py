from query_builder import *
from access import *


def query_builder_test():
    # Tests for the query builder module
    DATABASE = 'current'
    TABLETEST = ';DROP %^t!)e@(s#*t$& WHERE \\'
    TABLECONTROL = 'test'
    a = queryBuilder(DATABASE, TABLETEST)
    b = queryBuilder(DATABASE, TABLECONTROL)
    assert a.create_table() == b.create_table()
    assert a.insert_into_table(3) == b.insert_into_table(3)
    assert a.select_from_table() == b.select_from_table()
    assert a.update_into_table() == b.update_into_table()
    assert a.delete_from_table() == b.delete_from_table()


FIRST_ADD = ('AAPL', 27, 182.74)
SECOND_ADD = ('FARM', 85, 13.94)
THIRD_ADD = ('AAPL', 62, 39)
FOURTH_ADD = ('BB', 1793265, 91830562.70916523)
def access_testing():
    c = portfolioDB('want')
    c._setup_portfolio_table()
    c.add_to_portfolio_table(*FIRST_ADD)
    c.add_to_portfolio_table(*SECOND_ADD)
    c.add_to_portfolio_table(*THIRD_ADD)
    c.add_to_portfolio_table(*FOURTH_ADD)
    print('VIEWING TABLE BEFORE DELETION')
    c.see_portfolio_table()
    c.delete_from_portfolio_table('BB')
    print('VIEWING TABLE BEFORE DROP')
    c.see_portfolio_table()
    c.drop_portfolio_table()
    print('DELETING TABLE NOW')
    c.see_portfolio_table()
