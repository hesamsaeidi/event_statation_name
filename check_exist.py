from query import database_query
from query import select_query
import datetime
import math



def my_round(x):
    # my function to round int to 0.25
    return round(x*4)/4

def lat_lon_conv(lat, lon):
    co_lat = 90 - float(lat)
    new_lon = (float(lon) + 360) % 360
    return co_lat, new_lon


# defining the db in use
my_db = '/Users/hesam/test/db_test/all_data.db'

 # defining the query based on finding the location only
# my_query = '''SELECT
#                  id, e_id, date_time, lat, lon, depth
#              from
#                  events
#              where
#                  round(lat, 1) = {}
#                  and
#                  round(lon, 1) = {}'''

# query of searching for location needs 4 int as a square search
# in this order: min_lat, max_lat, min_lon, max_lon
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


with open('1B_events.txt', "r") as f:
    newEvents = f.readlines()

    for entry in newEvents:
        raw_list = entry.split()

        # create datetime obj for newEvents
        temp_date = [int(float(x)) for x in raw_list[0:6]]
        raw_dt_obj = datetime.datetime(*temp_date)

        # split lat and lon
        entry_lat , entry_lon = lat_lon_conv(*raw_list[6:8])
        min_lat = math.floor(entry_lat)
        max_lat = math.ceil(entry_lat)
        min_lon = math.floor(entry_lon)
        max_lon = math.ceil(entry_lon)
        # print(raw_list[6:8], "<<<<rrr>>>>",entry_lat, entry_lon, "\n",min_lat, max_lat, min_lon, max_lon)



        location_search_query = my_query.format(min_lat, max_lat, min_lon, max_lon)
        search_query = select_query(my_db, location_search_query)
        print(search_query)




# resutl = select_query(my_db, my_query)
# print(resutl)
#
#
# datetimeObj = datetime.datetime.strptime(resutl[0][1], '%Y-%m-%d %H:%M:%S.%f')
# print(">>>", datetimeObj)
