# coding=utf-8

from pymongo import MongoClient, DESCENDING
from bson.objectid import ObjectId
from datetime import datetime
import time

class BaseModel(object):
    client = MongoClient('localhost', 27017)
    db = client['disaster']

    def process_event(self, event):
        if event['latitude'] < 0:
            event['latitude_type'] = '南纬'
            event['latitude_num'] = -event['latitude']
        else:
            event['latitude_type'] = '北纬'
            event['latitude_num'] = event['latitude']

        if event['longitude'] < 0:
            event['longitude_type'] = '西经'
            event['longitude_num'] = -event['longitude']
        else:
            event['longitude_type'] = '东经'
            event['longitude_num'] = event['longitude']

        event["strtime"] = time.strftime("%Y-%m-%d %H:%M", time.localtime(event["timestamp"]))
        event["_id"] = str(event["_id"])
        return event

class IndexModel(BaseModel):
    def __init__(self):
        self.c_events = self.db['events']

    def get_earthquakes(self):
        quakes = []
        for event in self.c_events.find().sort("timestamp", DESCENDING).limit(3):
            event = self.process_event(event)
            quakes.append(event)
        return quakes


class DetailModel(BaseModel):
    def __init__(self):
        self.c_events = self.db['events']

    def get_detail(self, oid):
        return self.process_event(self.c_events.find_one({"_id": ObjectId(oid)}))

class AjaxDetailModel(BaseModel):
    def __init__(self):
        self.c_events = self.db['events']

    def get_events_in_range(self, latitude, longitude, timestamp, timerange):
        early_quakes = []
        late_quakes = []
        for event in self.c_events.find({
              "timestamp": {
                '$gt': timestamp - timerange,
                '$lt': timestamp + timerange
              },
              "longitude": {
                '$gte': longitude - 1,
                '$lte': longitude + 1,
              },
              "latitude": {
                '$gte': latitude - 1,
                '$lte': latitude + 1,
              }
            }):
            event = self.process_event(event)
            if event["timestamp"] > timestamp:
                late_quakes.append(event)
            else:
                early_quakes.append(event)
        return (early_quakes, late_quakes)


def test_indexModel():
    m = IndexModel()
    quakes = m.get_earthquakes()

    for q in quakes:
        print str(q["_id"])
        print q["_id"].__class__.__name__

def test_detailModel():
    m = DetailModel()
    print m.get_detail("5196f7eb3ac4505acab17e5f")

def test_ajaxDetailModel():
    m = AjaxDetailModel()
    print m.get_events_in_range(37.7, 124.7, 1368828120, 24*3600*7)

if __name__ == "__main__":
    #test_detailModel()
    test_ajaxDetailModel()
