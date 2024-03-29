# This scripts needs events.txt files with the NETWORKCODE_events.txt and all_data database
# It also needs query to be in the same folder as this scripts. Example of running command:
# $: python check_event.py IB 16
# IB is the NETWORKCODE and 16 is e_id in the database that shows the events related to this
# network added with e_id equal to 16.
# It goes through the txt file as the input and for each line in that it queries the db
# for events in the vicinity of the entry. In case there is no events in that location,
# a new entry will be inserted to the db. if there was one event at that location and time
# difference is smaller than t_delta, then it accepts the event_number and assign it to that
# entry. If there are more than one the one that is closer in time will be chosen.
# By Hesam Saeidi, June 2021, hsaeidi@crimson.ua.edu

from query import database_query
from query import select_query
from query import insert_query
import datetime
import math
import time
# from operator import itemgetter
import sys


# network name must be inserted as second arg
try:
    netwrok_name = str(sys.argv[1])
    event_id = int(sys.argv[2])
except IndexError:
    print("you need to insert network name!")
    sys.exit(1)

def my_round(x):
    # my function to round int to 0.25
    return round(x*4)/4

def lat_lon_conv(lat, lon):
    # lat and lon stored in master dataset as colatitude (0-180) and positive longitude (0-360)
    # for the sake of comparison this function convert the input lat and lon to the desired values
    co_lat = round(90 - float(lat),4)
    new_lon = round((float(lon) + 360) % 360, 4)
    return co_lat, new_lon

def write_to_file(dtobj, lat, lon, depth, evt_num):
    out_dt = dtobj.strftime("%Y %m %d %H %M %S")
    out_str = out_dt + " " + str(lat) + " " + str(lon) + " " + str(depth) + " " + str(evt_num) + "\n"
    with open(f"NETWORKS/EVT_WNUM/{netwrok_name}_events_wNums.txt", "a") as tempfile:
        tempfile.write(out_str)

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
                        {my_e_id}, \'{}\', 0, {}, {}, {}, 6, 0
                    )"""


with open(f'NETWORKS/EVENTS/{netwrok_name}_events.txt', "r") as f:
    newEvents = f.readlines()

    for entry in newEvents:
        # $yr," ",$mon," ",$day," ",$hr," ",$min," ",$sec," ",$elat," ",$elon," ",$edepth," ",$dummyMagn
        raw_list = entry.split()


        # create datetime obj for newEvents
        # temp_date = [int(float(x)) for x in raw_list[0:6]]
        # entry_dt_obj = datetime.datetime(*temp_date)
        yr, mon, day, hr, minute = [int(float(x)) for x in raw_list[0:5]]
        # The code checks if there is milisecond available or not
        try:
            sec, msec = raw_list[5].split(".")
        except ValueError:
            sec = raw_list[5]
            msec = 0
        # datetime ONLY accept integer and last placeholder is for microseconds
        entry_dt_obj = datetime.datetime(yr, mon, day, hr, minute, int(sec), int(msec)*1000)


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
                try:
                    # q_dt_obj = datetime.datetime.strptime(q[-1], '%Y-%m-%d %H:%M:%S.%f')
                    q_dt_obj = datetime.datetime.fromtimestamp(time.mktime(time.strptime(q[-1], '%Y-%m-%d %H:%M:%S.%f')))

                except ValueError:

                    q_dt_obj = datetime.datetime.strptime(q[-1], '%Y-%m-%d %H:%M:%S')
            except Exception as e:
                print("ERROR!!! ", e)
                pass
            if t_delta > abs(q_dt_obj - entry_dt_obj):
                close_events.append([q,abs(q_dt_obj - entry_dt_obj)])

        if len(close_events) == 0:
            ins_query = ev_insert_query.format(entry_dt_obj, entry_lat, entry_lon, entry_depth, my_e_id = event_id)
            Evnt_num = insert_query(my_db, ins_query)
            write_to_file(entry_dt_obj, entry_lat, entry_lon, entry_depth, Evnt_num)

        elif len(close_events) == 1:
            Evnt_num = close_events[0][0][0]
            write_to_file(entry_dt_obj, entry_lat, entry_lon, entry_depth, Evnt_num)

        else:
            desired_event = min(close_events,key=lambda x: x[1])
            # desired_event = min(close_events,key=itemgetter(1))
            Evnt_num = desired_event[0][0]
            write_to_file(entry_dt_obj, entry_lat, entry_lon, entry_depth, Evnt_num)
