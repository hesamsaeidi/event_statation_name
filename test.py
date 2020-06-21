import datetime
import time

# t = "2006-10-10 15:5:60.00"
# q_dt_obj = time.strptime(t, '%Y-%m-%d %H:%M:%S.%f')
# new_dt_obj = datetime.datetime.fromtimestamp(time.mktime(q_dt_obj))
# print(type(q_dt_obj), q_dt_obj)
# print(type(new_dt_obj), new_dt_obj)


# from query import insert_query
#
# #
# my_db = '/Users/hesam/test/db_test/all_data.db'
# # my_query = """ CREATE TABLE IF NOT EXISTS my_table (
# #                                         id integer PRIMARY KEY,
# #                                         num integer NOT NULL,
# #                                         tstr text NOT NULL
# #                                         ); """
# # database_query(my_db,my_query)
# query = """
#         INSERT INTO my_table(num, tstr)
#         VALUES(4,'cat')
#         """
# print(insert_query(my_db, query))


st_insert_query = """INSERT INTO stations(
                        num_row, name, lat, lon, elev, unkn1, unkn2)
                        VALUES(
                            {}, \'{}\', {}, {}, {}, 0, 0
                        )
                    """

a=st_insert_query.format(1,'s',2,3,4)
print(a)
