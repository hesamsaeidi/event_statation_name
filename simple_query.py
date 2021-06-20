from query import select_query
from pprint import pprint
my_db = '/Users/hesam/test/db_test/all_data.db'
# my_query = '''select
#                     id
#                 from
#                     events
#                 where
#                     CAST(strftime('%s', date_time)
#                     AS
#                     integer)
#                     >
#                     CAST(strftime('%s', '{}')
#                     AS
#                     integer)
#                     limit 5'''

# my_query = """SELECT
#                     COUNT(*) id
#                 FROM
#                     events
#                 WHERE
#                     lat
#                     BETWEEN '{}'
#                     AND '{}'
#                 AND
#                     lon
#                     BETWEEN '{}'
#                     AND '{}'"""

# my_query = """SELECT * from stations
#                 LIMIT 25"""
#
#
#
# resutl = select_query(my_db, my_query)
# print("first 25 rows: \n")
# pprint(resutl)
# print(my_query.format('2014-01-01 00:00:00', '2015-01-1 00:00:00'))


# my_query = """SELECT * from stations
#                 ORDER BY id DESC LIMIT 25"""



my_query = 'SELECT id from stations order by ID DESC limit 1'


nresutl = int(select_query(my_db, my_query)[0][0])
print(nresutl)
# print("last 25 rows: \n")
# pprint(nresutl)
