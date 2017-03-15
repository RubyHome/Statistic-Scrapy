import scrapy
import string

class proScraperSpider(scrapy.Spider):
    name = "statistic"
    url_template = "http://www.fleetwoodtoday.co.uk/search?query=%s&sortByFlag=true&sortBy=date"
    url_template2 = "http://www.fleetwoodtoday.co.uk/search?query=%s+%s&sortByFlag=true&sortBy=date"
    post_count = dict()
    total = dict()

    def start_requests(self):

        keyword_arr = ['fracking','earthquake', 'richter scale', 'Geology', 'Danger',
            'Shaking', 'Rumbling', 'Epicenter', 'Hypocenter', 'Wells', 'Drilling', 
            'Protest', 'Movement', 'Tremor', 'Quake', 'Seismic', 'Shock', 'Activity',
            # 'Cuadrilla*Drilling', 'fracking*earthquake', 'Danger*earthquake', 'fracking*wells',
            # 'fracking*drilling', 'fracking*geology', 'geology*earthquake', 'fracking*danger',
            # 'Cuadrilla*protest', 'fracking*activity', 'drilling*earthquake', 'drilling*activity',
            # 'houses*affected', 'houses*earthquake', 'houses*activity', 'houses*affected',
            # 'earthquake*affect', 'earthquake*effect', 'fracking*shock'
            ]
        url_template_arr = [
                'http://www.blackpoolgazette.co.uk/search?query=%s&sortByFlag=true&sortBy=date',
                'http://www.garstangcourier.co.uk/search?query=%s&sortByFlag=true&sortBy=date',
                'http://www.lythamstannesexpress.co.uk/search?query=%s&sortByFlag=true&sortBy=date',
                'http://www.lep.co.uk/search?query=%s&sortByFlag=true&sortBy=date',
                'http://www.fleetwoodtoday.co.uk/search?query=%s&sortByFlag=true&sortBy=date'
        ]
        for url_template in url_template_arr :
            self.total[url_template] = 0
            for keyword in keyword_arr:    
                self.post_count[keyword] = 0 
                
                # if "*" in keyword : 
                #     url = self.url_template2 % (keyword.split("*")[0], keyword.split("*")[1])
                # else :
                #     url = self.url_template % (keyword)

                url = url_template % (keyword)

                print(url)
                request = scrapy.Request(url=url, callback=self.parse)
                request.meta['keyword'] = keyword
                request.meta['url_template'] = url_template
                yield request

    def parse(self, response):
        keyword = response.meta['keyword']
        url_template = response.meta['url_template']

        for article in response.xpath('.//div[@id="google-search-results"]//article[@class="search-result-item"]'):
            title = article.xpath('.//a/text()').extract_first()
            date = article.xpath('.//span[@class="search-result-item__snippet"]/text()').extract_first()
            month = date.split(" ")[1]
            year = date.split(" ")[3]
            # print(month)
            # print(year)

            # ============ for each words ===================

            # if year == '2011' : 
            #     if month != 'Jan' or month != 'Feb' or month != 'Mar' :
            #         self.post_count[keyword] = self.post_count[keyword] + 1
            #         # print(keyword,'--------------',self.post_count[keyword])
            # if year == '2012' or year == '2013':
            #         self.post_count[keyword] = self.post_count[keyword] + 1
            #         # print(keyword,'--------------',self.post_count[keyword])
            # if year == '2014' : 
            #     if month == 'Jan' : 
            #         self.post_count[keyword] = self.post_count[keyword] + 1
            #         # print(keyword,'--------------',self.post_count[keyword]) 

            # ============ for each words ===================

             # ============ for apr 2011 - jan 2012 ==============
            if year == '2013' : 
                if month != 'Jan' or month != 'Feb' or month != 'Mar' :
                    self.total[url_template] = self.total[url_template] + 1
            if year == '2014' :
                if month == 'Jan' :                     
                    self.total[url_template] = self.total[url_template] + 1
            # ============ for apr 2011 - jan 2012 ==============


        for item in response.xpath('.//div[@class="google-search-pagination"]//a[@class="google-search-pagination__page"]'):
            # print("+++++++++++++++++++++++")
            # print(item.xpath('./@href').extract_first())

            detail_info = item.xpath('./@href').extract_first()
            request = scrapy.Request(detail_info, callback= self.parse_detail)
            request.meta['keyword'] = keyword
            request.meta['url_template'] = url_template
            yield request
    
    def parse_detail(self, response):
        keyword = response.meta["keyword"]
        url_template = response.meta['url_template']
        # print("keyword^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # print(keyword)
        # print("Here is parse_detail part")
        # print(response.url)
        # title = response.xpath('.//div[@id="google-search-results"]//article[@class="search-result-item"]')
        for article in response.xpath('.//div[@id="google-search-results"]//article[@class="search-result-item"]'):
            title = article.xpath('.//a/text()').extract_first()
            date = article.xpath('.//span[@class="search-result-item__snippet"]/text()').extract_first()
            month = date.split(" ")[1].strip()
            year = date.split(" ")[3].strip()
            # print(month)
            # print(year)
            # ============ for each words ===================

            # if year == '2011' : 
            #     if month != 'Jan' or month != 'Feb' or month != 'Mar' :
            #         self.post_count[keyword] = self.post_count[keyword] + 1
            #         # print(keyword,'--------------',self.post_count[keyword])
            # if year == '2012' or year == '2013':
            #         self.post_count[keyword] = self.post_count[keyword] + 1
            #         # print(keyword,'--------------',self.post_count[keyword])
            # if year == '2014' : 
            #     if month == 'Jan' : 
            #         self.post_count[keyword] = self.post_count[keyword] + 1
            #         # print(keyword,'--------------',self.post_count[keyword]) 

            # ============ for each words ===================

            # ============ for apr 2011 - jan 2012 ==============
            if year == '2013' : 
                if month != 'Jan' or month != 'Feb' or month != 'Mar' :
                    self.total[url_template] = self.total[url_template] + 1
            if year == '2014' :
                if month == 'Jan' :                     
                    self.total[url_template] = self.total[url_template] + 1
            # ============ for apr 2011 - jan 2012 ==============


#     http://www.blackpoolgazette.co.uk/
# http://www.garstangcourier.co.uk/
# http://www.lythamstannesexpress.co.uk/
# http://www.lep.co.uk/
# http://www.fleetwoodtoday.co.uk/


# Please data mine the following material:

# I am looking for papers with the keywords: Fracking, Earthquake, Richter Scale, Geology, Danger, Shaking, Rumbling, Epicenter, Hypocenter, Wells, Drilling, Cuadrilla, Protest, Movement, Tremor, Quake, Seismic, Shock, Activity

# Keywords with the phrase combination: Fracking and earthquake, danger and earthquake, Cuadrilla and drilling

# Please count the number of total papers for each newspaper post April 2011 to Jan 2012 and then from April 2012 to Jan 2013

# Please count the number of papers which contain any of the key words above for each newspaper post April 2011 to Jan 2012 and them from April 2012 to Jan 2013.

# Can you list all the information into excel.

# For example have headings for each and every different newspaper I have given
# List the key variables in rows and the number of times they appear for each paper as well as the date of the article in which they appear in
# List the number of total papers for the specific time periods I have provided