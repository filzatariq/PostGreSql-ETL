# PostGreSql-ETL
ETL Pipeline to read youtube data from json files and store it in tables

This project does a play analysis on youtube data that is stored in json files by writing the ETL to load the data from json files into database

Create_Table_queries.py contains the code for creating the tables and database. You need to run the python file Create_Tables.py to create these tables in your database.

The extract_transform_load.py file contains the ETL code for reading the data from the json files of data folder and populating the data into the created tables.

Run the extract_transform_load.py file and then finally run the test_tables.ipynb to ensure that the tables created successfully and data is populated 
