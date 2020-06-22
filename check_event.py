from query import database_query
from query import select_query
import datetime
import math
import time
from operator import itemgetter




def my_round(x):
    # my function to round int to 0.25
    return round(x*4)/4

def lat_lon_conv(lat, lon):
    # lat and lon stored in master dataset as colatitude (0-180) and positive longitude (0-360)
    # for the sake of comparison this function convert the input lat and lon to the desired values
    co_lat = 90 - float(lat)
    new_lon = (float(lon) + 360) % 360
    return co_lat, new_lon

t_delta = datetime.timedelta(minutes=5)
# defining the db in use
my_db = '/Users/hesam/test/db_test/all_data.db'

# query of searching for location needs 4 int as a square search
# in this order: min_lat, max_lat, min_lon, max_lon
ev_search_query = """SELECT
                    id, e_id, lat, lon, depth, date_time
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

ev_insert_query = """INSERT INTO
                        events(
                        e_id, date_time, hold, lat, lon, depth, magnitude, unkn
                    )
                    VALUES(
                        {}, {}, 0, {}, {}, {}, 6, 0
                    )"""


with open('NETWORKS/EVENTS/2H_events.txt', "r") as f:
    newEvents = f.readlines()

    for entry in newEvents:
        # $yr," ",$mon," ",$day," ",$hr," ",$min," ",$sec," ",$elat," ",$elon," ",$edepth," ",$dummyMagn
        raw_list = entry.split()


        # create datetime obj for newEvents
        temp_date = [int(float(x)) for x in raw_list[0:6]]
        entry_dt_obj = datetime.datetime(*temp_date)

        # split lat and lon
        entry_lat , entry_lon = lat_lon_conv(*raw_list[6:8])
        entry_depth = raw_list[8]

        # create the square search criteria
        min_lat = math.floor(entry_lat)
        max_lat = math.ceil(entry_lat)
        min_lon = math.floor(entry_lon)
        max_lon = math.ceil(entry_lon)



        location_search_query = ev_search_query.format(min_lat, max_lat, min_lon, max_lon)
        search_query = select_query(my_db, location_search_query)
        close_events = []
        for q in search_query:
            try:
                q_dt_obj = datetime.datetime.strptime(q[-1], '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                print(">>> ValueError for 60 seconds or 60 minutes:")
                q_dt_obj = datetime.datetime.fromtimestamp(time.mktime(time.strptime(q[-1], '%Y-%m-%d %H:%M:%S.%f')))

            if t_delta > abs(q_dt_obj - entry_dt_obj):
                close_events.append([q,abs(q_dt_obj - entry_dt_obj)])

        if len(close_events) == 0:
            print("nothing found! insert into database", entry)

        elif len(close_events) == 1:
            print("event found, extract info", q)

        else:
            desired_event = min(close_events,key=itemgetter(1))
            print(desired_event)
