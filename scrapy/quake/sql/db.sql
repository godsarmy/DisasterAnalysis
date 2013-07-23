CREATE TABLE quake (name TEXT, longtitude REAL, latitude REAL, timestamp INTEGER, depth REAL, magnitude REAL, source_url TEXT, PRIMARY KEY (timestamp, longtitude, latitude));
CREATE TABLE nation (longtitude REAL, latitude REAL, nation TEXT, PRIMARY KEY(longtitude, latitude));

CREATE TABLE iso3166 (nid TEXT, en_nation TEXT, cn_nation TEXT, PRIMARY KEY(nid));
CREATE TABLE operate_time (timestamp INTEGER, op_type TEXT, PRIMARY KEY(op_type));
