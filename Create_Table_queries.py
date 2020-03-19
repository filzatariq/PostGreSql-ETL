# DROP TABLES
# Write queries to drop each table, please don't change variable names,
# You should write respective queries against each varibale

#Note: I have populated data from JSON into normal tables and then build the 
#star_schema from these tables. Refer to test_tables to see the star schema

Videoplay_table_drop = "DROP TABLE IF EXISTS videoplay"
Users_table_drop = "DROP TABLE IF EXISTS users"
Videos_table_drop = "DROP TABLE IF EXISTS videos"
Youtubers_table_drop = "DROP TABLE IF EXISTS youtubers"
Time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
# Write queries to create each table, please don't change variable names, you can refer to star schema table
# You should write respective queries against each varibale

Videoplay_table_create = ("""CREATE TABLE IF NOT EXISTS videoplay \
    (videoplay_id SERIAL PRIMARY KEY, \
    start_time date NOT NULL, \
    user_id int NOT NULL, \
    level varchar, \
    video_id varchar, \
    youtuber_id varchar, \
    session_id smallint, \
    location varchar, \
    user_agent varchar);    
""")

Users_table_create = ("""CREATE TABLE IF NOT EXISTS users \
    (user_id int PRIMARY KEY, \
    first_name varchar NOT NULL, \
    last_name varchar NOT NULL, \
    gender varchar(1), \
    level varchar
    );
""")

Videos_table_create = ("""CREATE TABLE IF NOT EXISTS videos \
    (video_id varchar PRIMARY KEY, \
    title varchar NOT NULL, \
    youtuber_id varchar NOT NULL, \
    year int NOT NULL, \
    duration numeric NOT NULL
    );
""")


Youtubers_table_create = ("""CREATE TABLE IF NOT EXISTS youtubers \
    (youtuber_id varchar PRIMARY KEY, \
    name varchar NOT NULL, \
    location varchar, \
    latitude numeric, \
    longitude numeric
    );

""")

Time_table_create = ("""CREATE TABLE IF NOT EXISTS time \
    (start_time date PRIMARY KEY, \
    hour int NOT NULL, \
    day int NOT NULL, \
    week int NOT NULL, \
    month int NOT NULL, \
    year int NOT NULL, \
    weekday int NOT NULL   
    );

""")

# INSERT RECORDS
# Write queries to insert record to each table, please don't change variable names, you can refer to star schema table
# You should write respective queries against each varibale

Videoplay_table_insert = ("""INSERT INTO videoplay(start_time, user_id, level, video_id, youtuber_id, session_id, location, user_agent)\
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
""")

Users_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level)\
    VALUES(%s, %s, %s, %s, %s)\
    ON CONFLICT (user_id)\
    DO NOTHING;   
""")

Videos_table_insert = ("""INSERT INTO videos(video_id, title, youtuber_id, year, duration)\
    VALUES(%s, %s, %s, %s,%s)\
    ON CONFLICT(video_id)\
    DO NOTHING;
""")

Youtubers_table_insert = ("""INSERT INTO youtubers(youtuber_id, name, location, latitude, longitude)\
    VALUES(%s,%s,%s,%s,%s)\
    ON CONFLICT(youtuber_id)\
    DO NOTHING;
""")


Time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday)\
    VALUES(%s, %s, %s, %s, %s, %s, %s)\
    ON CONFLICT(start_time)\
    DO NOTHING;
""")



# QUERY LISTS

create_table_queries = [Users_table_create, Time_table_create, Youtubers_table_create, Videos_table_create, Videoplay_table_create]
drop_table_queries = [Videoplay_table_drop, Users_table_drop, Videos_table_drop, Youtubers_table_drop, Time_table_drop]
