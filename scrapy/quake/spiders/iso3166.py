# coding=utf-8

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

import re
import json
import sqlite3
import os


class ISO3166Spider(BaseSpider):
    name = "iso3166"
    allowed_domains = ["chacuo.net"]
    start_urls = ["http://doc.chacuo.net/iso-3166-1"]
    

    def parse(self, response):
        hxs = HtmlXPathSelector(text=response.body)
        tr_ele = hxs.select('//table[@class="f14"]/tbody/tr')

        spider_dir = os.path.dirname(os.path.realpath(__file__))
        settings = self.settings
        self.db_file = "%s/../%s" % (spider_dir, settings.get('DB_FILE'))

        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        for tr in tr_ele:
            td_ele = tr.select('td/text()')
            nid = td_ele[0].extract()
            en_nation = td_ele[4].extract()
            cn_nation = td_ele[5].extract().split(' ')[0]
            c.execute(
                "INSERT OR REPLACE INTO iso3166 VALUES (?,?,?)",
                [nid, en_nation, cn_nation]
            )
        conn.commit()

