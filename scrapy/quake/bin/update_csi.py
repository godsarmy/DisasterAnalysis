from pymongo import MongoClient
from datetime import datetime

import sqlite3
import os
import sys
import getopt


def update_quakes(conn, collection, full_dump=False):
    c = conn.cursor()

    sql = """
    SELECT q.*, n.cn_nation, n.nid FROM operate_time o, quake q LEFT JOIN (
        select na.latitude, na.longtitude, i.cn_nation, i.nid from nation na, iso3166 i where na.nation = i.nid
    ) AS n on q.latitude = n.latitude and q.longtitude = n.longtitude
    WHERE o.op_type = 'csi'
          """
    if not full_dump:
        sql += ' AND o.timestamp < q.timestamp'

    max_timestamp = 0
    total_inserted = 0

    for row in c.execute(sql):
        new_quake = {
            "name": row[0],
            "longitude": row[1],
            "latitude": row[2],
            "timestamp": row[3],
            "type": "earthquake",
            "source": "csi",
            "source_url": row[6],
            "details": {
                "depth": row[4],
                "magnitude": row[5],
            }
        }

        if row[7]:
            new_quake["nation"] = row[7]

        if row[8]:
            new_quake["nation_id"] = row[8]

        if max_timestamp < row[3]:
            max_timestamp = row[3]
        print new_quake
        collection.insert(new_quake)
        total_inserted += 1

    if max_timestamp > 0:
        insert_updated_time(conn, max_timestamp)

    print "total inserted: %d\n" % total_inserted


def insert_updated_time(conn, max_t):
    print max_t
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO operate_time (timestamp, op_type) VALUES (?,?)",
              [max_t, 'csi']
    )
    conn.commit()


def get_db_file():
    bin_dir = os.path.dirname(os.path.realpath(__file__))
    return bin_dir + '/../temp.db'


def get_events_collection():
    client = MongoClient('localhost', 27017)
    db = client['disaster']

    collection_events = db['events']
    return collection_events


if __name__ == '__main__':

    full_dump = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    for o, a in opts:
        if o == '-f':
            full_dump = True

    db_file = get_db_file()
    conn = sqlite3.connect(db_file)

    collection = get_events_collection()

    update_quakes(conn, collection, full_dump)
