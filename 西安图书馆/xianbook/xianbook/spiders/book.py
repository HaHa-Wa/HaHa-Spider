from scrapy import Spider, Request

from xianbook.items import BookItem


class BookSpider(Spider):
    name = 'book'
    page = 2

    # 修改原始请求
    def start_requests(self):
        url = f"http://139.9.135.174:8082/opac/search?q=*%3A*&searchType=standard&isFacet=true&view=standard&rows=10&sortWay=score&sortOrder=desc&curlibcode=CHANGAN&hasholding=1&searchWay0=marc&searchWay1=marc&searchWay2=marc&logical0=AND&logical1=AND&logical2=AND&page=1"

        yield Request(url, callback=self.parse)

    # 解析列表页面
    def parse(self, response):
        item = BookItem()
        # xpath 定位书籍列表
        books = response.xpath('//div[@id="resultTile"]/div[4]/table/tr')
        for book in books:
            # 使用xpath将各个字段取出
            div1 = ''.join(book.xpath('./td[4]/div[1]/div[1]//text()').getall()).replace('\t', '').split('\n')
            div1_id = book.xpath('./td[4]/div[1]/@bookrecno').get()
            div_1 = [x for x in div1 if x]
            bookName = div_1[0]
            if '已借' in div_1[1]:
                loansNum = div_1[1].replace('已借', '').replace('次.', '')
            else:
                loansNum = 0
            zhuzhe = book.xpath('//a[@class="author-link"]/text()').get().strip()
            div3 = ''.join(book.xpath('./td[4]/div[1]/div[3]//text()').getall()).replace('\t', '').split('\n')
            div_3 = [x for x in div3 if x]
            press = div_3[1]
            try:
                pressDate = div_3[3].replace('出版日期: ', '')
            except:
                press = ''
                pressDate = div_3[1].replace('出版日期: ', '')
            div5 = ''.join(book.xpath('./td[4]/div[1]/div[5]//text()').getall()).replace('\t', '').split('\n')
            div_5 = [x for x in div5 if x]
            try:
                leixing = div_5[1]
            except:
                leixing = ''
            try:
                shuhao = div_5[4]
            except:
                shuhao = ''
            item['bookName'] = bookName
            item['loansNum'] = loansNum
            item['zhuzhe'] = zhuzhe
            item['press'] = press
            item['pressDate'] = pressDate
            item['leixing'] = leixing
            item['shuhao'] = shuhao
            # 调用解析详情的方法 获取详情字段页面
            yield Request(f'http://139.9.135.174:8082/opac/book/{div1_id}?view=simple', callback=self.parseDetail,
                          meta={'data': item}, dont_filter=True, encoding='utf-8')

        # 循环调用parse 采集多页
        if BookSpider.page != 6392:
            url = f"http://139.9.135.174:8082/opac/search?q=*%3A*&searchType=standard&isFacet=true&view=standard&rows=10&sortWay=score&sortOrder=desc&curlibcode=CHANGAN&hasholding=1&searchWay0=marc&searchWay1=marc&searchWay2=marc&logical0=AND&logical1=AND&logical2=AND&page={BookSpider.page}"
            BookSpider.page += 1

            yield Request(url, callback=self.parse)

    # 解析详情页面
    def parseDetail(self, response):
        content_list = response.xpath('//*[@id="bookInfoTable"]/tr/td[@class="rightTD"]')

        timing = ''.join(content_list[0].xpath('.//text()').extract()).replace('\t', '').replace('\r', '').replace('\n',
                                                                                                                   '')
        isbn = ''.join(content_list[1].xpath('.//text()').extract()).replace('\t', '').replace('\r', '').replace('\n',
                                                                                                                 '')
        yuzhong = ''.join(content_list[2].xpath('.//text()').extract()).replace('\t', '').replace('\r', '').replace(
            '\n', '')
        xingtai = ''.join(content_list[3].xpath('.//text()').extract()).replace('\t', '').replace('\r', '').replace(
            '\n', '')
        faxing = ''.join(content_list[4].xpath('.//text()').extract()).replace('\t', '').replace('\r', '').replace('\n',
                                                                                                                   '')
        zhaiyao = ''.join(content_list[5].xpath('.//text()').extract()).replace('\t', '').replace('\r', '').replace(
            '\n', '')

        item = response.meta['data']
        item['timing'] = timing
        item['isbn'] = isbn
        item['yuzhong'] = yuzhong
        item['xingtai'] = xingtai
        item['faxing'] = faxing
        item['zhaiyao'] = zhaiyao
        # 将获取到的字段返回 传递给 piplines 并存入数据库
        yield item
