import psycopg2
from sql_queries import create_table_queries, drop_table_queries

config = {}
exec(open('config.py').read(), config)
user = config['user']
user2 = config['user2']
password = config['password']

def create_database():
    # connect to default database
    conn = psycopg2.connect(f"host=127.0.0.1 dbname=db1 user={user} password={password}")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    # cur.execute("")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect(f"host=127.0.0.1 dbname=sparkifydb user={user} password={password}")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
