
import sqlite3
import os
import sys

def update_timestamp(conn, max_t, op_type):
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO operate_time (timestamp, op_type) VALUES (?,?)",
              [max_t, op_type]
             )
    conn.commit()

def get_max(conn):
    c = conn.cursor()
    for row in c.execute("select max(timestamp) from quake"):
        return row[0]

def get_db_file():
    bin_dir = os.path.dirname(os.path.realpath(__file__))
    return bin_dir + '/../temp.db'

if __name__ == '__main__':
    db_file = get_db_file()
    conn = sqlite3.connect(db_file)

    max_timestamp = get_max(conn)
    update_timestamp(conn, max_timestamp, 'csi')
