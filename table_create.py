from query import database_query


my_db = '/Users/hesam/test/db_test/all_data.db'
my_query = """ CREATE TABLE IF NOT EXISTS events (
                                        id integer PRIMARY KEY,
                                        e_id integer NOT NULL,
                                        datetime text NOT NULL,
                                        hold integer NOT NULL,
                                        lat integer NOT NULL,
                                        lon integer NOT NULL,
                                        depth integer NOT NULL,
                                        magnitude integer NOT NULL,
                                        unkn integer NOT NULL

                                    ); """
database_query(my_db,my_query)
