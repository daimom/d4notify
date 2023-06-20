import scrapy
import requests
from ..items import D4NotifyItem
from datetime import datetime


class D4spiderSpider(scrapy.Spider):
    name = "d4spider"
    allowed_domains = ["diablo4.cc"]
    start_urls = ["https://diablo4.cc/"]

    def parse(self, response):
        self.log("url::: " + response.url)

        link = response.url + 'tw/'
        yield scrapy.Request(link, callback=self.parse_time)

    def parse_time(self,response):
        item = D4NotifyItem()
        # item['d4event']=response.xpath('//h4/div/text()').extract_first()
        item['d4event']=response.css('body > div.page > div > div.row.row-cols-1.row-cols-lg-3 > div:nth-child(2) > div > div.card-header::text').get()
        # self.log("event = "+item['d4event'])
        item['d4boss']=response.css('body > div.page > div > div.row.row-cols-1.row-cols-lg-3 > div:nth-child(2) > div > div.collapse.show > div > div:nth-child(2)::text').get()
        unixtime=response.css('body > div.page > div > div.row.row-cols-1.row-cols-lg-3 > div:nth-child(2) > div > div.collapse.show > div > div:nth-child(1)::attr(data-displaytime)').get()
        item['takePlace'] = datetime.fromtimestamp(int(unixtime)).strftime('%Y-%m-%d %H:%M:%S')
        msg = item['d4event']+ " : "+item['d4boss'] +" 將在 " + item['takePlace'] +  "出現"
        self.lineNotifyMessage(msg)
        # item['takePlace']=response.xpath('//html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/@data-displaytime').get()
        # self.log("發生時間="+item['takePlace'])


    def lineNotifyMessage(self,msg):

      headers = {
          "Authorization": "Bearer <token>",
          "Content-Type" : "application/x-www-form-urlencoded"
      }

      payload = {'message': msg}
      r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
      return r.status_code