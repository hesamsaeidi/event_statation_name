from datetime import datetime
import time

t = "2006-10-10 15:5:50.00"
q_dt_obj = datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f')
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

#
# st_insert_query = """INSERT INTO stations(
#                         num_row, name, lat, lon, elev, unkn1, unkn2)
#                         VALUES(
#                             {}, \'{}\', {}, {}, {}, 0, 0
#                         )
#                     """
#
# a=st_insert_query.format(1,'s',2,3,4)
# print(a)
# gen = [[3,1], [4,0.5], [5,0.25]]
# from operator import itemgetter
# l = min(gen,key=itemgetter(1))
# print(l)

# dateStr = q_dt_obj.strftime("%Y %m %d %H %M %S")
# print(dateStr)
def write_to_file(dtobj, lat, lon, depth, evt_num):
    out_dt = dtobj.strftime("%Y %m %d %H %M %S")
    out_str = out_dt + " " + str(lat) + " " + str(lon) + " " + str(depth) + " " + str(evt_num) + "\n"
    with open("events_wNums.txt", "a") as tempfile:
        tempfile.write(out_str)

write_to_file(q_dt_obj, 12.999, 90.01, 12, 3348334)
write_to_file(q_dt_obj, 17.69, 90.01, 1.02, 3341998)
write_to_file(q_dt_obj, 19.29, 9.81, 19, 137434)
