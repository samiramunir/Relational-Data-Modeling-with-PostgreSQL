import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *



def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = (df.song_id.values[0], df.title.values[0],
             df.artist_id.values[0], int(df.year.values[0]),
             float(df.duration.values[0]))
    cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_data = (df.artist_id.values[0], df.artist_name.values[0],
               df.artist_location.values[0], df.artist_latitude.values[0],
               df.artist_longitude.values[0])
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df.query('page == "NextSong"')

    # convert timestamp column to datetime
    df.iloc[:, 15] = pd.to_datetime(df.ts, unit = 'ms')

    # insert time data records
    time_df = pd.DataFrame()
    time_df['ts'] = df['ts']
    time_df['hour'] = df['ts'].dt.hour
    time_df['day'] = df['ts'].dt.day
    time_df['weekofyear'] = df['ts'].dt.hour
    time_df['month'] = df['ts'].dt.month
    time_df['year'] = df['ts'].dt.hour
    time_df['weekday'] = df['ts'].dt.weekday

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = pd.DataFrame()
    user_df['user_id'] = df.userId
    user_df['first_name'] = df.firstName
    user_df['last_name'] = df.lastName
    user_df['gender'] = df.gender
    user_df['level'] = df.level

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (index, row.ts, row.userId,
                            row.level, songid,
                            artistid, row.sessionId,
                            row.location, row.userAgent)

    cur.execute(songplay_table_insert, songplay_data)
    cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


config = {}
exec(open('config.py').read(), config)
user = config['user']
password = config['password']

def main():
    conn = psycopg2.connect(f"host=127.0.0.1 dbname=sparkifydb user={user} password={password}")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
