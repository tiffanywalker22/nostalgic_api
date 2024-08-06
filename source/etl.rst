ETL Script
==========

Overview
--------

Describe what the ETL script does.

Functions
---------

- `connect_db()`: Connects to the PostgreSQL database.
- `create_table()`: Creates the `bedrooms` table if it does not exist.
- `delete_all_data()`: Deletes all existing data from the `bedrooms` table so that new data can be added
- `insert_bedroom()`: Inserts new data from the CSV file into the `bedrooms` table.
- `process_csv()`: Processes CSV data so that it can be added to the database.