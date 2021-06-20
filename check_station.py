from query import database_query
from query import select_query
from query import insert_query
import datetime
import sys
import math
import time

# network name must be inserted as second arg
try:
    netwrok_name = str(sys.argv[1])
except IndexError:
    print("you need to insert network name!")
    sys.exit(1)


def lat_lon_conv(lat, lon):
    # lat and lon stored in master dataset as colatitude (0-180) and positive longitude (0-360)
    # for the sake of comparison this function convert the input lat and lon to the desired values
    co_lat = 90 - float(lat)
    new_lon = (float(lon) + 360) % 360
    return co_lat, new_lon

def my_round(x):
    # my function to round int to 0.25
    return round(x*4)/4


def location_checker(lat_1, lon_1, lat_2, lon_2):
    r_lat_1 = my_round(lat_1)
    r_lon_1 = my_round(lon_1)
    r_lat_2 = my_round(lat_2)
    r_lon_2 = my_round(lon_2)
    if r_lat_1 == r_lat_2 and r_lon_1 == r_lon_2:
        return True
    else:
        return False



my_db = '/Users/hesam/test/db_test/all_data.db'

lastrowid_query = 'SELECT id from stations order by ID DESC limit 1'
last_num_row = int(select_query(my_db, lastrowid_query)[0][0])


st_search_query = """SELECT
                id, num_row, name, lat, lon
            FROM
                stations
            WHERE
                name = '{}' """

st_insert_query = """INSERT INTO stations(
                        num_row, name, lat, lon, elev, unkn1, unkn2)
                        VALUES(
                            {}, \'{}\', {}, {}, {}, 0, 0
                        )
                    """

station_dict = {}
with open(f'NETWORKS/STATIONS/{netwrok_name}_sta_evt_predTT.out', "r") as f:
    newStats = f.readlines()

    for entry in newStats:
        raw_list = entry.split()
        # $yr," ",$mon," ",$day," ",$hr," ",$min," ",$sec," ",$sta," ",$elat," ",$elon," ",$edep," ",$stlat," ",$stlon," ",$stel," ",$az," ",$garc," ",$pickT," ",$obsTT," ",$predTT," ",$rayParam
        # ['2012', '10', '17', '04', '42', '31.60', 'AKWI', '4.179', '124.561', '338.4', '1.0368', '36.31', '0.871', '270.901', '88.1813', '300.837', '733.777', '733.15', '4.680']
        if len(raw_list) != 19:
            pass
        else:
            station_name = raw_list[6]
            if not station_name in station_dict:
                entry_lat , entry_lon = lat_lon_conv(*raw_list[10:12])
                station_search_query = st_search_query.format(station_name)
                search_query = select_query(my_db, station_search_query)

                if len(search_query) == 1:
                    if location_checker(entry_lat , entry_lon, search_query[0][3], search_query[0][4]):
                        station_dict[station_name] = search_query[0][0]
                    else:
                        # query to insert new
                        st_elev = float(raw_list[12])
                        last_num_row = last_num_row + 1
                        my_query = st_insert_query.format(last_num_row,station_name,entry_lat , entry_lon, st_elev)
                        station_dict[station_name] = insert_query(my_db, my_query)


                elif len(search_query) == 0:
                    # query to insert new
                    st_elev = float(raw_list[12])
                    last_num_row = last_num_row + 1
                    my_query = st_insert_query.format(last_num_row,station_name,entry_lat , entry_lon, st_elev)
                    station_dict[station_name] = insert_query(my_db, my_query)


                else:
                    # more than one stations with the same name
                    for q in search_query:
                        if location_checker(entry_lat, entry_lon, q[3], q[4]):
                            station_dict[station_name] = q[0]
                            break
                    if not station_name in station_dict:
                        # query to insert new
                        st_elev = float(raw_list[12])
                        last_num_row = last_num_row + 1
                        my_query = st_insert_query.format(last_num_row,station_name,entry_lat , entry_lon, st_elev)
                        station_dict[station_name] = insert_query(my_db, my_query)
                        print('no match!!')

print('>>>>>>',station_dict)
