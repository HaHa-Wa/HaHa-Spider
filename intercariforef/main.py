# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/14 10:19 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import requests
from bs4 import BeautifulSoup

cookies = {
    'SSESS2ac2cf2f1261f24829db8476862cebea': 'w0CyCS6Wtz-gdTXOOTgOKWvA_QVJW2EkDedivY_njcU',
}

headers = {
    # 'Host': 'www.intercariforef.org',
    # 'cache-control': 'max-age=0',
    # 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"macOS"',
    # 'upgrade-insecure-requests': '1',
    # 'origin': 'https://www.intercariforef.org',
    # 'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'sec-fetch-site': 'same-origin',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-user': '?1',
    # 'sec-fetch-dest': 'document',
    # 'referer': 'https://www.intercariforef.org/formations/recherche-formations.html?init=0',
    # 'accept-language': 'zh-CN,zh;q=0.9',
}


def main():
    # data = 'region=&code-departements=&mots-cles=agriculteur&lib-commune=Toulouse&form_build_id=form-PS5xSeJyhUEM-PC7Wg-EBEVXAgpSN-z3rOa9C8YOWO4&form_id=simple_search_formation_form&op=Rechercher'
    list1 = ['agriculture', 'BTP']
    list2 = ["Paris", 'Toulouse']
    for l1 in list1:
        for l2 in list2:
            data = {
                "region": "",
                "code-departements": "",
                "mots-cles": l1,
                "lib-commune": l2,
                'form_build_id': 'form-NpO5O8EdIsJFlj8WhZSVgVEy_bbwD9pDqTz_HFvyJjY',
                'form_id': 'simple_search_formation_form',
                'op': "Rechercher"
            }
            print(data)
            url = 'https://www.intercariforef.org/formations/recherche-formations.html?init=0'
            response = requests.post(url, headers=headers, data=data)
            print(response.status_code)
            res = BeautifulSoup(response.text, 'lxml')
            div_ = res.find('div', id='box')
            tbody = div_.find('tbody')
            trs = tbody.find_all('tr')
            print(len(trs))
            for tr in trs:
                # print(tr)
                tds = tr.find_all('td')
                id = tds[0].text
                detail_url = "https://www.intercariforef.org" + tds[1].text
                titre = tds[2].text
                Dep = tds[4].text
                Ville = tds[5].text
                Derniere_session = tds[8].text
                Organisme = tds[9].text
                Publics = tds[10].text
                # print(id, detail_url, titre, Dep, Ville, Derniere_session, Organisme, Publics)


def get_detail():
    url = 'https://www.intercariforef.org/formations/accompagnement-vae/competence-commerce-et-international/formation-15_622883_1209616.html'
    ret = requests.get(url, headers=headers)
    res = BeautifulSoup(ret.text, 'lxml')
    title_div = res.find('div', class_='col-md-12 boffreinfo-content')
    title_p = title_div.find('p').text.strip()
    title_h1 = title_div.find('h1').text.strip()
    print(title_p, '-' * 20)
    print(title_h1, '-' * 20)
    cards = res.find('div', id='accordion')
    # cards = cards.find_all("div", class_='card')
    # for card in cards:
    #     h4_info = card.find('h4').text.strip()
    collapseCertifs = cards.find('div', id='collapseCertifs').text.strip()
    collapseObjectifs = cards.find('div', id='collapseObjectifs').text.strip()
    collapseMetiers = cards.find('div', id='collapseMetiers').text.strip()
    collapseDuree = cards.find('div', id='collapseDuree').text.strip()
    collapseConditionAcces = cards.find('div', id='collapseConditionAcces').text.strip()
    collapseLieuReal = cards.find('div', id='collapseLieuReal').text.strip()
    collapsePeriode = cards.find('div', id='collapsePeriode').text.strip()
    collapseOresp = cards.find('div', id='collapseOresp').text.strip()

    print(collapseObjectifs)
    print(collapseCertifs)
    print('-' * 20)


if __name__ == '__main__':
    main()
    # get_detail()
