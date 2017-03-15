# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class StatisticscraperPipeline(object):
    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
    	print spider.total
    	my_dict = spider.total	
        with open('post-sum2013-2014.csv', 'wb') as f:  # Just use 'w' mode in 3.x
		    w = csv.DictWriter(f, my_dict.keys())
		    w.writeheader()
		    w.writerow(my_dict)
    	# ============ for each words ===================
      #   print spider.post_count
      #   my_dict = spider.post_count	
      #   with open('mycsvfile-fleetwoodtoday.csv', 'wb') as f:  # Just use 'w' mode in 3.x
		    # w = csv.DictWriter(f, my_dict.keys())
		    # w.writeheader()
		    # w.writerow(my_dict)
		# ============ for each words ===================    

    def process_item(self, item, spider):
        return item
