import sqlite3

from sqlite3 import Error


def database_query(db_file, query):

    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        # rows = c.description
        print("1: ",rows)

        # for row in rows:
        #     print(row)
    except Error as e:
        print('error: ', e)


my_db = '/Users/hesam/test/db_test/all_data.db'
my_query = "select * from events where id<100"
# my_query = "SELECT name FROM sqlite_master WHERE type='table';"

database_query(my_db,my_query)
