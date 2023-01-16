import json
import time
import urllib

import scrapy
from bs4 import BeautifulSoup
from scrapy.http import JsonRequest

from inter.items import InterItem


class SearchSpider(scrapy.Spider):
    name = 'search'

    def start_requests(self):

        url = 'https://www.baidu.com/'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, *arg, **kwargs):
        list1 = ['agriculture', 'BTP']
        list2 = ["Paris", 'Toulouse']
        haha = []
        for l1 in list1:
            for l2 in list2:
                # print(l1, l2)
                haha.append([l1, l2])
        while haha:
            ha = haha.pop()
            data = {
                # "region": "",
                # "code-departements": "",
                "mots-cles": ha[0],
                "lib-commune": ha[1],
                'form_build_id': 'form-NpO5O8EdIsJFlj8WhZSVgVEy_bbwD9pDqTz_HFvyJjY',
                'form_id': 'simple_search_formation_form',
                'op': "Rechercher"
            }
            url = 'https://www.intercariforef.org/formations/recherche-formations.html?init=0'
            yield scrapy.FormRequest(url, formdata=data,
                                     callback=self.parse_two,
                                     method="POST",
                                     dont_filter=True,
                                     meta={'data': data})

    def parse_two(self, response, *arg, **kwargs):
        data = response.meta['data']
        if response.status == 403:
            url = 'https://www.intercariforef.org/formations/recherche-formations.html?init=0'

            yield scrapy.FormRequest(url, formdata=data,
                                     callback=self.parse_two,
                                     method="POST",
                                     dont_filter=True,
                                     meta={'data': data})
        res = BeautifulSoup(response.text, 'lxml')
        div_ = res.find('div', id='box')
        tbody = div_.find('tbody')
        trs = tbody.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            id = tds[0].text
            detail_url = "https://www.intercariforef.org" + tds[1].text
            titre = tds[2].text
            Dep = tds[4].text
            Ville = tds[5].text
            Derniere_session = tds[8].text
            Organisme = tds[9].text
            Publics = tds[10].text
            one_info = InterItem()
            one_info['id'] = id
            one_info['detail_url'] = detail_url
            one_info['titre'] = titre
            one_info['Dep'] = Dep
            one_info['Ville'] = Ville
            one_info['Derniere_session'] = Derniere_session
            one_info['Organisme'] = Organisme
            one_info['Publics'] = Publics
            # yield one_info
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'one_info': one_info})

    def parse_detail(self, response, *arg, **kwargs):
        one_info = response.meta['one_info']
        res = BeautifulSoup(response.text, 'lxml')
        title_div = res.find('div', class_='col-md-12 boffreinfo-content')
        title_p = title_div.find('p').text.strip()
        title_h1 = title_div.find('h1').text.strip()
        print(title_p, '-' * 20)
        print(title_h1, '-' * 20)
        cards = res.find('div', id='accordion')

        try:
            collapseCertifs = cards.find('div', id='collapseCertifs').text.strip()
        except:
            collapseCertifs = ''
        try:
            collapseObjectifs = cards.find('div', id='collapseObjectifs').text.strip()
        except:
            collapseObjectifs = ''
        try:
            collapseMetiers = cards.find('div', id='collapseMetiers').text.strip()
        except:
            collapseMetiers = ''
        try:
            collapseDuree = cards.find('div', id='collapseDuree').text.strip()
        except:
            collapseDuree = ''
        try:
            collapseConditionAcces = cards.find('div', id='collapseConditionAcces').text.strip()
        except:
            collapseConditionAcces = ''
        try:
            collapseLieuReal = cards.find('div', id='collapseLieuReal').text.strip()
        except:
            collapseLieuReal = ''
        try:
            collapsePeriode = cards.find('div', id='collapsePeriode').text.strip()
        except:
            collapsePeriode = ''
        try:
            collapseOresp = cards.find('div', id='collapseOresp').text.strip()
        except:
            collapseOresp = ''
        one_info['collapseCertifs'] = collapseCertifs
        one_info['collapseObjectifs'] = collapseObjectifs
        one_info['collapseMetiers'] = collapseMetiers
        one_info['collapseDuree'] = collapseDuree
        one_info['collapseConditionAcces'] = collapseConditionAcces
        one_info['collapseLieuReal'] = collapseLieuReal
        one_info['collapsePeriode'] = collapsePeriode
        one_info['collapseOresp'] = collapseOresp
        yield one_info
