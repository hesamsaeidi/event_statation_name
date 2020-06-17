from query import database_query
my_db = '/Users/hesam/test/db_test/all_data.db'
with open('masterSta.list', "r") as f:
    masterSta = f.readlines()

    for i, entry in enumerate(masterSta):
        # print(entry.split())
        name, lat, lon, elev, unkn1, unkn2 = entry.split()
        my_query = f'''INSERT INTO stations(
                    num_row, name, lat, lon, elev, unkn1, unkn2) VALUES
                        ({i+1}, \'{name}\', {lat}, {lon}, {elev}, {unkn1}, {unkn2})
                        '''
        # print(my_query, i)
        database_query(my_db,my_query)
        # break
