# coding=utf-8

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

import re
import time
import sqlite3
import os

class CSISpider(BaseSpider):
    name = "csi"
    allowed_domains = ["csi.ac.cn"]
    base_url = "http://www.csi.ac.cn"

    def get_last_timestamp(self, db_file):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        sql = "select timestamp from operate_time where op_type = 'csi'"
        for row in c.execute(sql):
            return row[0]
        conn.close()

    def start_requests(self):
        spider_dir = os.path.dirname(os.path.realpath(__file__))
        settings = self.settings
        self.db_file = "%s/../%s" % (spider_dir, settings.get('DB_FILE'))
        print self.db_file

        self.last_timestamp = self.get_last_timestamp(self.db_file)

        yield Request(
            "http://www.csi.ac.cn/manage/html/4028861611c5c2ba0111c5c558b00001/_SUBAO/index.html",
            self.parse
        )

    def get_epoch(self, t):
        epoch = 0
        time_str = t.split('.')[0]
        try:
            date = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            epoch = time.mktime(date)
        except:
            try:
                date = time.strptime(time_str, "%Y-%m-%d %H:%M")
                epoch = time.mktime(date)
            except:
                print "failed to convert %s" % time_str
        return epoch

    def parse(self, response):
        oneday = 24*3600
        lines = response.body.split("\n")
        for line in lines:
            found = re.search('var str = "(.+)"', line)
            if found:
                i = 0
                epoch = 0
                for e in found.group(1).split("~"):
                    i += 1
                    if (i % 4 == 0):
                        epoch = self.get_epoch(e)
                    if (i % 4 == 1):
                        url = "%s/%s" % (self.base_url, e)
                        if epoch == 0 or epoch > (self.last_timestamp - oneday):
                            yield Request(url, callback=self.item_parse)

    def item_parse(self, response):
        hxs = HtmlXPathSelector(text=response.body)
        page_ele = hxs.select('//div[@class="memo"]/text()')
        if len(page_ele) > 0:
            text = page_ele[0].extract()
            result = re.search(ur"北京时间(.+) 在(.+)\((.+),(.+)\) 发生(.+)级地震，震源深度(.+)公里", text, re.UNICODE)
            #print result.group(1), result.group(2), result.group(3), result.group(4), result.group(5), result.group(6)

            epoch = time.mktime(time.strptime(result.group(1), "%Y-%m-%d %H:%M"))
            if (epoch < self.last_timestamp):
                return

            name = result.group(2)
            magnitude = result.group(5)
            depth = result.group(6)

            latitude_re = re.search(r"([^\d]+)(\d+\.\d+)", result.group(3))
            latitude = float(latitude_re.group(2)) if latitude_re.group(1) == u"北纬" else 0 - float(latitude_re.group(2))
            longtitude_re = re.search(r"([^\d]+)(\d+\.\d+)", result.group(4))
            longtitude = float(longtitude_re.group(2)) if longtitude_re.group(1) == u"东经" else 0 - float(longtitude_re.group(2))
            #print latitude, longtitude

            db_file = self.db_file
            conn = sqlite3.connect(db_file)
            c = conn.cursor()
            print "insert %s to %f, %f\n" % (name, latitude, longtitude)
            c.execute("INSERT OR REPLACE INTO quake (name, longtitude, latitude, timestamp, depth, magnitude, source_url) VALUES (?,?,?,?,?,?,?)", 
                        [name, longtitude, latitude, epoch, depth, magnitude, response.url]
                     )

            conn.commit()
