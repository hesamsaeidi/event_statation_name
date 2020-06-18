from query import database_query
from query import select_query
import datetime
import math
import time



def lat_lon_conv(lat, lon):
    # lat and lon stored in master dataset as colatitude (0-180) and positive longitude (0-360)
    # for the sake of comparison this function convert the input lat and lon to the desired values
    co_lat = 90 - float(lat)
    new_lon = (float(lon) + 360) % 360
    return co_lat, new_lon


my_db = '/Users/hesam/test/db_test/all_data.db'

my_query = """SELECT
                id, num_row, name, lat, lon
            FROM
                stations
            WHERE
                name = '{}' """


with open('2H_sta_evt_predTT.out', "r") as f:
    newEvents = f.readlines()

    for entry in newEvents:
        raw_list = entry.split()
        # e.g. raw_list = ['2012', '10', '17', '04', '42', '31.60', 'AKWI', '4.179', '124.561', '338.4', '1.0368', '36.31', '0.871', '270.901', '88.1813', '300.837', '733.777', '733.15', '4.680']
        # $yr," ",$mon," ",$day," ",$hr," ",$min," ",$sec," ",$sta," ",$elat," ",$elon," ",$edep," ",$stlat," ",$stlon," ",$stel," ",$az," ",$garc," ",$pickT," ",$obsTT," ",$predTT," ",$rayParam
        # print(raw_list[6], raw_list[10:12])
        entry_lat , entry_lon = lat_lon_conv(*raw_list[10:12])
        station_search_query = my_query.format(raw_list[6])
        search_query = select_query(my_db, station_search_query)
        if search_query:
            # print(search_query, entry_lat , entry_lon)
            for q in search_query:
                if round(q[3],2) == round(entry_lat,2):
                    if round(q[4],2) == round(entry_lon,2):
                        print("station found!", q[2])
