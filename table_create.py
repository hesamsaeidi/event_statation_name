from query import database_query


my_db = '/Users/hesam/test/db_test/all_data.db'
my_query = """ CREATE TABLE IF NOT EXISTS events (
                                        id integer PRIMARY KEY,
                                        e_id integer NOT NULL,
                                        date_time text NOT NULL,
                                        hold integer NOT NULL,
                                        lat integer NOT NULL,
                                        lon integer NOT NULL,
                                        depth integer NOT NULL,
                                        magnitude integer NOT NULL,
                                        unkn integer NOT NULL

                                    ); """
database_query(my_db,my_query)


# stations_table_query = """ CREATE TABLE IF NOT EXISTS stations (
#                                         id integer PRIMARY KEY,
#                                         num_row integer NOT NULL,
#                                         name text NOT NULL,
#                                         lat integer NOT NULL,
#                                         lon integer NOT NULL,
#                                         elev integer NOT NULL,
#                                         unkn1 integer NOT NULL,
#                                         unkn2 integer NOT NULL
#
#                                     ); """
#
# database_query(my_db, stations_table_query)
