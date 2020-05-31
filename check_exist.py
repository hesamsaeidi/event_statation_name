from query import database_query
from query import select_query
from datetime import timedelta

my_db = '/Users/hesam/test/db_test/all_data.db'
my_query = 'SELECT id,datetime, lat, lon, depth from events where round(lat,1)=42.7 and round(lon) = 13'
resutl = select_query(my_db, my_query)
print(resutl)




with open('1B_events.txt', "r") as f:
    newEvents = f.readlines()

    for entry in newEvents:
        print(entry.split())
