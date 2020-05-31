import sqlite3
from pprint import pprint
conn = sqlite3.connect('test_dataset_master.db')


c = conn.cursor()

c.execute('''
                SELECT * from events
            ''')

c.execute('''
                INSERT INTO events VALUES ('1', '2009-01-01', '10:35:26.2222222', '-23', '90', '12', 6.5)
            ''')

conn.commit()
conn.close()


conn = sqlite3.connect('test_dataset_master.db')
c = conn.cursor()


c.execute('''
                SELECT * from events;
            ''')
pprint(c.fetchall())

conn.close()
