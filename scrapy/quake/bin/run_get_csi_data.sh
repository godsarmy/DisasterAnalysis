#!/bin/bash

echo "start at `date`"
scrapy crawl csi
scrapy crawl nation
python update_csi.py
