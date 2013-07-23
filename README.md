DisasterAnalysis
================

The project to analyze disaster such as earthquake, tsunami, typhoon, etc

[![main page](https://raw.github.com/godsarmy/DisasterAnalysis/master/screenshot/main.png)](#features)

* Guide:

1. Install Mongodb (http://www.mongodb.org/)

2. Install Scrapy for python (http://scrapy.org/)

3. Install Tornado (http://www.tornadoweb.org)

4. Install Pymongo (http://api.mongodb.org/python/current)

* Start mongodb:

  $ mongod

* Gather inform:

  $ cd scrapy/quake/bin

  $ ./run_get_csi_data.sh

* Start web server:

  $ ./demo.py
