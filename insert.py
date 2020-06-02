from query import database_query
my_db = '/Users/hesam/test/db_test/all_data.db'
with open('masterEvt.list', "r") as f:
    masterEvt = f.readlines()

    for entry in masterEvt:
        # print(entry.split())
        ID, year, month, day, hold, hour, min, sec, lat, lon, depth, magnt, unkn = entry.split()
        i_datetime = f"{year}-{month}-{day} {hour}:{min}:{sec}"
        my_query = f'''INSERT INTO events(
                    e_id, date_time, hold, lat, lon, depth, magnitude, unkn) VALUES
                        ({ID}, \'{i_datetime}\', {hold}, {lat}, {lon}, {depth}, {magnt}, {unkn})
                        '''
        print(my_query)
        database_query(my_db,my_query)
