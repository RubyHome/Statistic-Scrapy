import scrapy
import string

class proScraperSpider(scrapy.Spider):
    name = "statistic"
    url_template = "http://www.blackpoolgazette.co.uk/search?query=%s&sortByFlag=true&sortBy=date"
    post_count = dict()
    total = 0
    # def __init__(self):
    #     self.keyword = "fracking"
    #     self.post_count = 0

    def start_requests(self):

        keyword_arr = ['fracking'
        ,'earthquake', 'richter scale', 'Geology', 'Danger',
            'Shaking', 'Rumbling', 'Epicenter', 'Hypocenter', 'Wells', 'Drilling', 
        #     'Protest', 'Movement', 'Tremor', 'Quake', 'Seismic', 'Shock', 'Activity',
        #     'Cuadrilla Drilling', 'fracking earthquake', 'Danger earthquake', 'fracking wells',
        #     'fracking drilling', 'fracking geology', 'geology earthquake', 'fracking danger',
        #     'Cuadrilla protest', 'fracking activity', 'drilling earthquake', 'drilling activity',
        #     'houses affected', 'houses earthquake', 'houses activity', 'houses affected',
        #     'earthquake affect', 'earthquake effect', 'fracking shock'
            ]
        url_template_arr = [
                'http://www.blackpoolgazette.co.uk/search?query=%s&sortByFlag=true&sortBy=date',
                'http://www.garstangcourier.co.uk/search?query=%s&sortByFlag=true&sortBy=date',
                'http://www.lythamstannesexpress.co.uk/search?query=%s&sortByFlag=true&sortBy=date',
                'http://www.lep.co.uk/search?query=%s&sortByFlag=true&sortBy=date',
                'http://www.fleetwoodtoday.co.uk/search?query=%s&sortByFlag=true&sortBy=date'
        ]
        
        for keyword in keyword_arr:    
            self.post_count[keyword] = 0 
            url = self.url_template % (keyword)
            # url = 'http://www.blackpoolgazette.co.uk/search?query=fracking&sortByFlag=true&sortBy=date'
            request = scrapy.Request(url=url, callback=self.parse)
            request.meta['keyword'] = keyword
            yield request

        # result print
        for keyword in keyword_arr : 
            print(keyword, '--------------', self.post_count[keyword])



    def parse(self, response):
        keyword = response.meta['keyword']
        for article in response.xpath('.//div[@id="google-search-results"]//article[@class="search-result-item"]'):
            title = article.xpath('.//a/text()').extract_first()
            date = article.xpath('.//span[@class="search-result-item__snippet"]/text()').extract_first()
            month = date.split(" ")[1]
            year = date.split(" ")[3]
            # print(month)
            # print(year)
            if year == '2011' : 
                if month != 'Jan' or month != 'Feb' or month != 'Mar' or month != 'Apr' :
                    self.post_count[keyword] = self.post_count[keyword] + 1
                    # print(keyword,'--------------',self.post_count[keyword])
            if year == '2012' :
                if month != 'Feb' or month != 'Mar' : 
                    self.post_count[keyword] = self.post_count[keyword] + 1
                    # print(keyword,'--------------',self.post_count[keyword])
            if year == '2013' : 
                if month == 'Jan' : 
                    self.post_count[keyword] = self.post_count[keyword] + 1
                    # print(keyword,'--------------',self.post_count[keyword])

        for item in response.xpath('.//div[@class="google-search-pagination"]//a[@class="google-search-pagination__page"]'):
            # print("+++++++++++++++++++++++")
            # print(item.xpath('./@href').extract_first())

            detail_info = item.xpath('./@href').extract_first()
            request = scrapy.Request(detail_info, callback= self.parse_detail)
            request.meta['keyword'] = keyword
            yield request
    
    def parse_detail(self, response):
        keyword = response.meta["keyword"]
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
            if year == '2011' : 
                if month != 'Jan' or month != 'Feb' or month != 'Mar' or month != 'Apr' :
                    self.post_count[keyword] = self.post_count[keyword] + 1
                    # print(keyword,'--------------',self.post_count[keyword])
            if year == '2012' :
                if month != 'Feb' or month != 'Mar' : 
                    self.post_count[keyword] = self.post_count[keyword] + 1
                    # print(keyword,'--------------',self.post_count[keyword])
            if year == '2013' : 
                if month == 'Jan' : 
                    self.post_count[keyword] = self.post_count[keyword] + 1
                    # print(keyword,'--------------',self.post_count[keyword]) 

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