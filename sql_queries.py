# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES


songplay_table_create = ("""
                            CREATE TABLE IF NOT EXISTS
                                songplays (songplay_id int PRIMARY KEY, start_time timestamp,
                                            user_id int NOT NULL, level text,
                                            song_id varchar, artist_id varchar,
                                                session_id int, location text,
                                            user_agent text)
""")

user_table_create = ("""
                            CREATE TABLE IF NOT EXISTS
                                users (user_id int PRIMARY KEY, first_name text,
                                        last_name text, gender text,
                                        level text)

""")

song_table_create = ("""
                            CREATE TABLE IF NOT EXISTS
                                songs (song_id varchar PRIMARY KEY, title text,
                                        artist_id varchar NOT NULL, year int,
                                        duration numeric)
""")

artist_table_create = ("""
                            CREATE TABLE IF NOT EXISTS
                                artists (artist_id varchar PRIMARY KEY , name text,
                                            location text, latitude numeric,
                                            longitude numeric)
""")

time_table_create = ("""
                            CREATE TABLE IF NOT EXISTS
                            time (start_time timestamp PRIMARY KEY, hour int, day int,
                                    week int, month int, year int,
                                    weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time,
                                                    user_id, level, song_id,
                                                    artist_id, session_id,
                                                    location, user_agent)
                                            values (%s, %s, %s, %s, %s,
                                                    %s, %s, %s, %s)
                                                    ON CONFLICT (songplay_id)
                                                    DO NOTHING;
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name,
                                            gender, level)
                                            values (%s, %s, %s, %s, %s)
                                            ON CONFLICT (user_id)
                                            DO NOTHING;
""")

song_table_insert = (""" INSERT INTO songs (song_id, title, artist_id,
                                            year, duration)
                                            values (%s, %s, %s, %s, %s)
                                            ON CONFLICT (song_id)
                                            DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location,
                                                latitude, longitude)
                                                values (%s, %s, %s, %s, %s)
                                                ON CONFLICT (artist_id)
                                                DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day,
                                            week, month, year, weekday)
                                            values (%s, %s, %s, %s, %s, %s, %s)
                                            ON CONFLICT (start_time)
                                            DO NOTHING;
""")

# FIND SONGS

song_select = (""" SELECT S.song_id, S.artist_id
                        FROM songs S JOIN artists A
                        ON S.artist_id = A.artist_id
                        WHERE
                                S.title = %s
                                AND
                                A.name = %s
                                AND
                                S.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
