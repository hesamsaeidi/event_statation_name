#!/usr/bin/env python

# This code query the db for all the events added after a specific id and create
# a allEvent.out file with the proper format as before.
# This script is need to be run once per inserting new data no matter how many networks.
# By Hesam Saeidi, June 2021, hsaeidi@crimson.ua.edu

from query import select_query
my_db = '/Users/hesam/test/db_test/all_data.db'



def write_to_file(evt_num, year, month, day, hr, minute, second, lat, lon, depth, magnitude):
    # copy from Sam's code in perl; output should be like this
    # printf OUT (" %6i   %4i  %2i  %2i   %1i  %2i  %2i  %2.2f   %2.3f   %3.3f   %3.1f  %1.1f  0.0\n",$evtNumb,$yr,$mon,$day,$hold,$hr,$min,$sec,$elat,$elon,$edepth,$mgn);
    hold = 0
    lat = float(lat)
    lon = float(lon)
    depth = float(depth)
    magnitude = float(magnitude)
    second = float(second)
    evt_num = int(evt_num)
    year = int(year)
    month = int(month)
    day = int(day)
    hr = int(hr)
    minute = int(minute)
    raw_str = " {:6d}   {:4d}  {:2d}  {:2d}   {:1d}  {:2d}  {:2d}  {:.2f}   {:.3f}   {:.3f}   {:.1f}  {:.1f}  0.0\n"
    out_str = raw_str.format(evt_num, year, month, day, hold, hr, minute, second, lat, lon, depth, magnitude)
    # out_str =" "+evt_num+"   "+year+"  "+month+day+hold+hr+minute+second+lat+lon+" "+depth+" "+magnitude+"\n"
    with open(f"NETWORKS/ALLEVENTS/allEvents.out", "a") as tempfile:
        tempfile.write(out_str)


allEvents_query = """SELECT
                    id, date_time, lat, lon, depth, magnitude
                FROM
                    events
                WHERE
                    id > 553165
                    """


allEvents_result = select_query(my_db, allEvents_query)
# print(len(allEvents_result), allEvents_result[0])

for evn in allEvents_result:
    #(553166, '2006-06-05 00:50:21', 72.008, 119.075, 124, 6)
    evt_num, date_time, lat, lon, depth, mag = evn
    ev_date, ev_time = date_time.split(' ')
    yr, month, day = ev_date.split('-')
    hr, minute, second = ev_time.split(':')
    write_to_file(evt_num, yr, month, day,hr, minute, second, lat, lon, depth, mag)
    # print(evt_num, date_time, lat, lon, depth, mag)
