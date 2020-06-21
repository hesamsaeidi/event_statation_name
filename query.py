import sqlite3

from sqlite3 import Error


def database_query(db_file, query):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    except Error as e:
        print('error: ', e)

    finally:
        if conn:
            conn.close()



def select_query(db_file, query):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(query)
        return c.fetchall()
    except Error as e:
        print('error: ', e)

    finally:
        if conn:
            conn.close()


def insert_query(db_file, query):
    # returns lastrowid
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        return c.lastrowid
    except Error as e:
        print('error: ', e)

    finally:
        if conn:
            conn.close()
