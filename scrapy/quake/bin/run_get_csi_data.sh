#!/bin/bash

current_dir=`dirname $0`
echo "start at `date`"
scrapy crawl csi
scrapy crawl nation
echo python $current_dir/update_csi.py
