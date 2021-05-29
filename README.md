## **Before Running**
These scripts create a SQL database with python and test output results for matching events and stations
The final output will be traveltime residuls for event-station pairs with unique numbers for events
All these codes were only tested on mac 
SQlite is used because it is already installed by default

## **Database Creation**
### table_create.py:
will check if the two tables exists in the database or not.

If it is not already created it will create them
### init.py: 
initialize the connection to the main database which is named all_data.db

