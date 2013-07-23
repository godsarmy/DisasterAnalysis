# coding=utf-8

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

import re
import json
import sqlite3

class Nation2Spider(BaseSpider):
    name = "nation2"
    allowed_domains = ["geonames.org"]
    base_url = "http://ws.geonames.org/countryCode?lat=%f&lng=%f"
    
    def start_requests(self):
        settings = self.settings
        self.db_file = settings.get('DB_FILE')

        sql = """
        select latitude, longtitude from quake q where not exists 
        (select * from nation n where n.longtitude = q.longtitude and n.latitude = q.latitude)
              """

        start_urls = []
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        for row in c.execute(sql):
            start_urls.append(self.base_url % (row[0], row[1]))

        conn.commit()
        conn.close()

        #yield Request(start_urls[2], self.parse)
        for url in start_urls:
            yield Request(url, self.parse)

    def parse(self, response):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        result = re.search(r"=([\d\.\-]+),([\d\.\-]+)", response.url)
        if len(response.body) < 10:
            print response.body
        """
        if len(json_data["results"]) > 0:
            address = json_data["results"][0]["address_components"]
            for comp in address:
                if len(comp["types"]) > 0 and comp["types"][0] == 'country':
                    nation = comp["long_name"]
                    print result.group(1), result.group(2), nation
                    c.execute("INSERT OR REPLACE INTO nation (latitude, longtitude, nation) VALUES (?,?,?)", 
                                [result.group(1), result.group(2), nation]
                    )
                    break
        """
        conn.commit()

