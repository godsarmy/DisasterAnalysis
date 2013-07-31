"""
Handlers
"""

import tornado.web
from tornado.escape import json_encode

import model

# files to store handlers
class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.model = model.IndexModel()

    def get(self):
        self.render("index.tpl",
                    project_name=self.settings["globals"]["project_name"],
                    app_name="index-map",
                    moduleName="",
                    events=self.model.get_earthquakes()
                   )


class DetailHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.model = model.DetailModel()

    def get(self):
        oid = self.get_argument('id')
        self.render("detail.tpl",
                    project_name=self.settings["globals"]["project_name"],
                    app_name="detail-map",
                    moduleName="",
                    event=self.model.get_detail(oid)
                   )

class AjaxDetailHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.model = model.AjaxDetailModel()

    def get(self):
        latitude = float(self.get_argument('latitude'))
        longitude = float(self.get_argument('longitude'))
        timestamp = int(self.get_argument('timestamp'))
        timerange = 24 * 3600 * 7

        (early_quakes, late_quakes) = self.model.get_events_in_range(latitude, longitude, timestamp, timerange)
        self.write(json_encode({"early_events": early_quakes, "late_events": late_quakes}))

class StatisticsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("statistics.tpl",
                    project_name=self.settings["globals"]["project_name"],
                    app_name="statistics-map",
                   )
