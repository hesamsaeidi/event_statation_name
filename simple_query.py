from query import select_query

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

my_query = """SELECT
                    COUNT(*) id
                FROM
                    events
                WHERE
                    lat
                    BETWEEN '{}'
                    AND '{}'
                AND
                    lon
                    BETWEEN '{}'
                    AND '{}'"""




resutl = select_query(my_db, my_query.format('77', '87', '98', '109'))
print(resutl)
# print(my_query.format('2014-01-01 00:00:00', '2015-01-1 00:00:00'))
