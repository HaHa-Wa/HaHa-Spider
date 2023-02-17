import retrying
from scrapy import Request, Spider
from bs4 import BeautifulSoup
import requests


class SpiderSpider(Spider):
    name = 'spider'
    allowed_domains = ['myflixer.to']
    start_urls = ['http://myflixer.to/']

    def start_requests(self):
        url_list = []
        for page in range(1, 369):
            print('page:  ', page)
            url = 'https://myflixer.to/tv-show?page={0}'.format(page)
            url_list.append(url)
        for url in url_list:
            yield Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        bs_ret = BeautifulSoup(response.text, 'lxml')
        film_list_wrap = bs_ret.find('div', class_='film_list-wrap')
        flw_item = film_list_wrap.find_all('div', class_='flw-item')
        for item in flw_item:
            # print(item)
            h2 = item.find('h2', class_='film-name').find('a')
            title = h2['title']
            href = 'https://myflixer.to' + h2['href']
            print(title, href)
            one_info = {
                'title': title,
                'href': href
            }
            if title == '0号宿舍':
                continue
            yield Request(href, callback=self.get_detail, meta={'info': one_info})

            # get_detail(title, href)

    def get_detail(self, response, **kwargs):
        info = response.meta['info']
        href = info['href']
        title = info['title']
        bs_ret = BeautifulSoup(response.text, 'lxml')
        detail_page = bs_ret.find('div', class_='detail_page-infor')
        pingfen = detail_page.find('button', class_='btn btn-sm btn-radius btn-warning btn-imdb').text
        description = detail_page.find('div', class_='description').text
        # print(pingfen, description)
        elements = detail_page.find('div', class_='elements')
        # print(elements)
        row_line = elements.find_all('div', class_='row-line')
        Released = row_line[0].text.replace('   ', '').replace('\n', '')
        Genre = row_line[1].text.replace('   ', '').replace('\n', '')
        Duration = row_line[2].text.replace('   ', '').replace('\n', '')
        Country = row_line[3].text.replace('   ', '').replace('\n', '')
        Production = row_line[4].text.replace('   ', '').replace('\n', '')
        Casts = row_line[5].text.replace('   ', '').replace('\n', '')
        # print(Released, Genre, Duration, Country, Production, Casts)
        mv_id = href[href.rfind('-') + 1:]
        one_info = {
            'title': title,
            'pingfen': pingfen,
            'mv_id': mv_id,
            'description': description,
            'Released': Released,
            'Genre': Genre,
            'Duration': Duration,
            'Country': Country,
            'Production': Production,
            'Casts': Casts,
            'href': href,
        }
        info_url = 'https://myflixer.to/ajax/v2/tv/seasons/' + str(mv_id)
        yield Request(info_url, callback=self.get_info, meta={'one_info': one_info})

    def get_info(self, response, **kwargs):
        bs_ret = BeautifulSoup(response.text, 'lxml')
        one_info = response.meta['one_info']
        id_divs = bs_ret.find_all('a', class_='dropdown-item ss-item')
        all_juji = []
        for div in id_divs:
            href = 'https://myflixer.to/ajax/v2/season/episodes/' + div['data-id']
            juji = div.text
            title_list = self.get_session_list(href)
            # title_list = await Request(href, callback=self.get_session_list)
            all_juji.append({
                juji: title_list
            })
        one_info['all_juji'] = all_juji
        yield one_info

    def get_session_list(self, url):
        # headers = {
        #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        # }
        # ret = requests.get(url, headers=headers)

        bs_ret = send_req(url)
        lis = bs_ret.find_all('li', class_='nav-item')
        title_list = []
        for li in lis:
            a_ = li.find('a')
            title = a_['title']
            # print(title)
            title_list.append(title)
        return title_list

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

@retrying.retry(stop_max_attempt_number=10, wait_fixed=2000)
def send_req(url):
    ret = requests.get(url, headers=headers, timeout=5)
    bs_ret = BeautifulSoup(ret.text, 'lxml')
    return bs_ret

# def get_session_list(url):
#     # url = 'https://myflixer.to/ajax/v2/season/episodes/73618'
#

#     ret = requests.get(url, headers=headers)
#     bs_ret = BeautifulSoup(ret.text, 'lxml')
#     lis = bs_ret.find_all('li', class_='nav-item')
#     title_list = []
#     for li in lis:
#         a_ = li.find('a')
#         title = a_['title']
#         # print(title)
#         title_list.append(title)
#     return title_list
