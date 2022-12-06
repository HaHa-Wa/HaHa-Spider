import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from retrying import retry


def get_proxy():
    headers = {
        'authority': 'www.icourse163.org',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    ret = requests.get(
        'https://proxy.qg.net/extract?Key=代理IPkey&Num=1&AreaId=&Isp=&DataFormat=json&DataSeparator=&Detail=0',
        headers=headers)
    ret_json = ret.json()['Data'][0]

    return {
        'https': f"{ret_json['IP']}:{ret_json['port']}"
    }


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def job_detail(job_href):
    print(job_href)
    cookies = {
        '_uab_collina': '167014271042131523959228',
        'guid': '45576bde9b1521fa60e855399bdb43d3',
        'nsearch': 'jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
        'ps': 'needv%3D0',
        'privacy': '1670139697',
        '51job': 'cuid%3D218218873%26%7C%26cusername%3DR1ZpNhTLtyrkPon3vwOnAFOx%252FECUtKqz9J3rA41Gv4k%253D%26%7C%26cpassword%3D%26%7C%26cname%3DfqEadcwKbVIQe%252BFc7W1CDQ%253D%253D%26%7C%26cemail%3D%26%7C%26ccry%3D.0BRyEw4Srrdk%26%7C%26cenglish%3D0%26%7C%26to%3D174da2455832768d713ca7e6e78ceef0637d876a%26%7C%26',
        'slife': 'lowbrowser%3Dnot%26%7C%26lastlogindate%3D20221204%26%7C%26securetime%3DUm4ANQBgAm9SMVZvCDJbMFtpAjE%253D',
        'partner': 'www_google_com',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22218218873%22%2C%22first_id%22%3A%22184a257dbe6e00-029e06522c3f35c-18525635-2007040-184a257dbe789d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg0YTI1N2RiZTZlMDAtMDI5ZTA2NTIyYzNmMzVjLTE4NTI1NjM1LTIwMDcwNDAtMTg0YTI1N2RiZTc4OWQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIyMTgyMTg4NzMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22218218873%22%7D%2C%22%24device_id%22%3A%22184a257dbe6e00-029e06522c3f35c-18525635-2007040-184a257dbe789d%22%7D',
        'search': 'jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CF%FA%CA%DB%B2%BF%BE%AD%C0%ED%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60020000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21',
        'acw_tc': 'ac11000116701484310946963e00df691ef7e6667dc48eea27104ce2ef3930',
        'ssxmod_itna': 'YqjxBQi=0=deqGKGHivnrFD7+KYYve5GOFmFICDBuor4iNDnD8x7YDvmIhQnmKnAiwhPfbAOnpPsK0RxiFdkSiwINfnGZ+eD=xYQDwxYoDUxGtDpxG6dqmDYAkDt4DTD34DYDiEC8cBdqQDCxDFDljcnqDEDYPlDA3Di4D+0TtDmudDGdKDbqQDIqN4KrqqxBo=rwjS0q4x1GramqGyAPGuWq6q5CX/FwHxOW+baEWolODqmYxFK2xq/D4mY74p5gDYR0GphKExC7xqR7dsjiqDGShsUiD==',
        'ssxmod_itna2': 'YqjxBQi=0=deqGKGHivnrFD7+KYYve5GOFmFGD8daCxGXKqGaKCbmk1om1KBoC=7mQY/e4w5ezqCOT9Y5lQnCxt=Vi4pydpwlhEoXNk1110yHD8oSGLGTLnEqc3yZFOcgUbsdtiBliF8MBI8a2vGw6I1Vg0aE=07S69=loE8afGGOzw=MPc8rg05pou8UcAE9piEib9wqEyaU=cw+4eeH=+Fvhb7LowxeQ+dqgSWKMudum9QGgAEuQcha=PuuifbDtctEa6dHdudm78eRiShwZRjxym+qnpqUWEmDOCNNPbESUHsN6yt0uzl2aWTj8H8tYECcafpEeA6lxEWmgI4nFu7I+LbBAAhK3R//5Kg2iG0vRuiFAVWqnRBzK+eM5teyzWR=nYQrYk8vktHY=i3D07iho8Ox50w/GAPLG=BorbCo7eD7=DYIKeD',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': '_uab_collina=167014271042131523959228; guid=45576bde9b1521fa60e855399bdb43d3; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; ps=needv%3D0; privacy=1670139697; 51job=cuid%3D218218873%26%7C%26cusername%3DR1ZpNhTLtyrkPon3vwOnAFOx%252FECUtKqz9J3rA41Gv4k%253D%26%7C%26cpassword%3D%26%7C%26cname%3DfqEadcwKbVIQe%252BFc7W1CDQ%253D%253D%26%7C%26cemail%3D%26%7C%26ccry%3D.0BRyEw4Srrdk%26%7C%26cenglish%3D0%26%7C%26to%3D174da2455832768d713ca7e6e78ceef0637d876a%26%7C%26; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20221204%26%7C%26securetime%3DUm4ANQBgAm9SMVZvCDJbMFtpAjE%253D; partner=www_google_com; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22218218873%22%2C%22first_id%22%3A%22184a257dbe6e00-029e06522c3f35c-18525635-2007040-184a257dbe789d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg0YTI1N2RiZTZlMDAtMDI5ZTA2NTIyYzNmMzVjLTE4NTI1NjM1LTIwMDcwNDAtMTg0YTI1N2RiZTc4OWQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIyMTgyMTg4NzMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22218218873%22%7D%2C%22%24device_id%22%3A%22184a257dbe6e00-029e06522c3f35c-18525635-2007040-184a257dbe789d%22%7D; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CF%FA%CA%DB%B2%BF%BE%AD%C0%ED%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60020000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; acw_tc=ac11000116701484310946963e00df691ef7e6667dc48eea27104ce2ef3930; ssxmod_itna=YqjxBQi=0=deqGKGHivnrFD7+KYYve5GOFmFICDBuor4iNDnD8x7YDvmIhQnmKnAiwhPfbAOnpPsK0RxiFdkSiwINfnGZ+eD=xYQDwxYoDUxGtDpxG6dqmDYAkDt4DTD34DYDiEC8cBdqQDCxDFDljcnqDEDYPlDA3Di4D+0TtDmudDGdKDbqQDIqN4KrqqxBo=rwjS0q4x1GramqGyAPGuWq6q5CX/FwHxOW+baEWolODqmYxFK2xq/D4mY74p5gDYR0GphKExC7xqR7dsjiqDGShsUiD==; ssxmod_itna2=YqjxBQi=0=deqGKGHivnrFD7+KYYve5GOFmFGD8daCxGXKqGaKCbmk1om1KBoC=7mQY/e4w5ezqCOT9Y5lQnCxt=Vi4pydpwlhEoXNk1110yHD8oSGLGTLnEqc3yZFOcgUbsdtiBliF8MBI8a2vGw6I1Vg0aE=07S69=loE8afGGOzw=MPc8rg05pou8UcAE9piEib9wqEyaU=cw+4eeH=+Fvhb7LowxeQ+dqgSWKMudum9QGgAEuQcha=PuuifbDtctEa6dHdudm78eRiShwZRjxym+qnpqUWEmDOCNNPbESUHsN6yt0uzl2aWTj8H8tYECcafpEeA6lxEWmgI4nFu7I+LbBAAhK3R//5Kg2iG0vRuiFAVWqnRBzK+eM5teyzWR=nYQrYk8vktHY=i3D07iho8Ox50w/GAPLG=BorbCo7eD7=DYIKeD',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    # response = requests.get(job_href, cookies=cookies, headers=headers, proxies=get_proxy(), timeout=5)
    response = requests.get(job_href, cookies=cookies, headers=headers, timeout=5)
    try:
        res = response.content.decode(encoding='gbk')
    except:
        res = response.content.decode(encoding='utf-8')
    # print(res)
    bs_html = BeautifulSoup(res, 'lxml')
    print(bs_html)
    content = bs_html.find('div', class_='tBorderTop_box')
    try:
        print(content.text)
        return content.text
    except:
        df = pd.DataFrame(job_list)
        df.to_excel('数据分析师2.xls')


def get_info():
    cookies = {
        '_uab_collina': '166917098372563287554808',
        'guid': '45576bde9b1521fa60e855399bdb43d3',
        'nsearch': 'jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
        'ps': 'needv%3D0',
        'privacy': '1670139697',
        '51job': 'cuid%3D218218873%26%7C%26cusername%3DR1ZpNhTLtyrkPon3vwOnAFOx%252FECUtKqz9J3rA41Gv4k%253D%26%7C%26cpassword%3D%26%7C%26cname%3DfqEadcwKbVIQe%252BFc7W1CDQ%253D%253D%26%7C%26cemail%3D%26%7C%26ccry%3D.0BRyEw4Srrdk%26%7C%26cenglish%3D0%26%7C%26to%3D174da2455832768d713ca7e6e78ceef0637d876a%26%7C%26',
        'slife': 'lowbrowser%3Dnot%26%7C%26lastlogindate%3D20221204%26%7C%26securetime%3DUm4ANQBgAm9SMVZvCDJbMFtpAjE%253D',
        'partner': 'www_google_com',
        'acw_tc': 'ac11000116701397072302272e00e1e3618a46af49bac359eb254c6cab052a',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22218218873%22%2C%22first_id%22%3A%22184a257dbe6e00-029e06522c3f35c-18525635-2007040-184a257dbe789d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg0YTI1N2RiZTZlMDAtMDI5ZTA2NTIyYzNmMzVjLTE4NTI1NjM1LTIwMDcwNDAtMTg0YTI1N2RiZTc4OWQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIyMTgyMTg4NzMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22218218873%22%7D%2C%22%24device_id%22%3A%22184a257dbe6e00-029e06522c3f35c-18525635-2007040-184a257dbe789d%22%7D',
        'acw_sc__v2': '638c52e8a737654c34d854aab77d57f4405acffa',
        'search': 'jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CF%FA%CA%DB%B2%BF%BE%AD%C0%ED%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60020000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21',
        'ssxmod_itna': 'eqUx0DgDcDBDu0WqGHD8AqG=vrcmLiYfDmOfuBeGXxpoDZDiqAPGhDC88U+opnGm4qQYAbAwTeii+cGsjWRCGhefQ714bD=xYQDwxYoDUxGtDpxG6TIDen=D5xGoDPxDeDAQ/QSSwZ40PD7EXRbMtDm4GWfqGfDDoDYfUyDitUDDU7DY=XD7USR0xqKeGvUnQ2mLU3/kGeag=DzdFDtq=uYeilnd6CVd2jUbnolhhoWGP5KGxel0xiIGm5RGh39GxwH9D5YEDK9Be+qyDDG833i8DxD=',
        'ssxmod_itna2': 'eqUx0DgDcDBDu0WqGHD8AqG=vrcmLiYfDmOfuDA6nxPp3D/7iRDFEOLtuh7DzAa=D6B0r6xQ/OG0i=5uAmnik8G6kAn40Aau0r40YEB9ys9Qf1GrnGOtBEcUpp3QdWwehT+EwN5PODQehDzq7iFtYYYREpiOQIH=b4qQ4IwXomhcWhq2mgd7Oeo/imq73pqmmAHrzAGiFT+tFwWo=LW3A7jcGGUc/SU9fKO4wk=9t9XszmtC4qLk/q1W4Fi42eWtpgkawiTzckx=ZFBWU6tV0mizyxQfX9NaQeToxnWcW=IwpWm1IcxihtAoiBr320KHM7UkYRdofwoZ8Qgoozdho2C9DQae+RBzHCYMkh4Eh0Ai3WzTeKAlHIeQnhCVAo3l=zEzRoCRxQiLHiTvRgrNdvxZ=lwOlmFl8ABTEPpAQ=AGdICdIcQQRooOrhKEfbhLHcf0jL3Wj9W3awOKbEvcEr8E6ZAjpO/QfiLAa669Z7EDDwphYDI/Cm3Yhk0D2gHPW=XnDU=3kADeWhjZKKwN5sm/DGcDG7KiDD==',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': '_uab_collina=166917098372563287554808; guid=45576bde9b1521fa60e855399bdb43d3; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; ps=needv%3D0; privacy=1670139697; 51job=cuid%3D218218873%26%7C%26cusername%3DR1ZpNhTLtyrkPon3vwOnAFOx%252FECUtKqz9J3rA41Gv4k%253D%26%7C%26cpassword%3D%26%7C%26cname%3DfqEadcwKbVIQe%252BFc7W1CDQ%253D%253D%26%7C%26cemail%3D%26%7C%26ccry%3D.0BRyEw4Srrdk%26%7C%26cenglish%3D0%26%7C%26to%3D174da2455832768d713ca7e6e78ceef0637d876a%26%7C%26; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20221204%26%7C%26securetime%3DUm4ANQBgAm9SMVZvCDJbMFtpAjE%253D; partner=www_google_com; acw_tc=ac11000116701397072302272e00e1e3618a46af49bac359eb254c6cab052a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22218218873%22%2C%22first_id%22%3A%22184a257dbe6e00-029e06522c3f35c-18525635-2007040-184a257dbe789d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg0YTI1N2RiZTZlMDAtMDI5ZTA2NTIyYzNmMzVjLTE4NTI1NjM1LTIwMDcwNDAtMTg0YTI1N2RiZTc4OWQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIyMTgyMTg4NzMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22218218873%22%7D%2C%22%24device_id%22%3A%22184a257dbe6e00-029e06522c3f35c-18525635-2007040-184a257dbe789d%22%7D; acw_sc__v2=638c52e8a737654c34d854aab77d57f4405acffa; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CF%FA%CA%DB%B2%BF%BE%AD%C0%ED%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60020000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; ssxmod_itna=eqUx0DgDcDBDu0WqGHD8AqG=vrcmLiYfDmOfuBeGXxpoDZDiqAPGhDC88U+opnGm4qQYAbAwTeii+cGsjWRCGhefQ714bD=xYQDwxYoDUxGtDpxG6TIDen=D5xGoDPxDeDAQ/QSSwZ40PD7EXRbMtDm4GWfqGfDDoDYfUyDitUDDU7DY=XD7USR0xqKeGvUnQ2mLU3/kGeag=DzdFDtq=uYeilnd6CVd2jUbnolhhoWGP5KGxel0xiIGm5RGh39GxwH9D5YEDK9Be+qyDDG833i8DxD=; ssxmod_itna2=eqUx0DgDcDBDu0WqGHD8AqG=vrcmLiYfDmOfuDA6nxPp3D/7iRDFEOLtuh7DzAa=D6B0r6xQ/OG0i=5uAmnik8G6kAn40Aau0r40YEB9ys9Qf1GrnGOtBEcUpp3QdWwehT+EwN5PODQehDzq7iFtYYYREpiOQIH=b4qQ4IwXomhcWhq2mgd7Oeo/imq73pqmmAHrzAGiFT+tFwWo=LW3A7jcGGUc/SU9fKO4wk=9t9XszmtC4qLk/q1W4Fi42eWtpgkawiTzckx=ZFBWU6tV0mizyxQfX9NaQeToxnWcW=IwpWm1IcxihtAoiBr320KHM7UkYRdofwoZ8Qgoozdho2C9DQae+RBzHCYMkh4Eh0Ai3WzTeKAlHIeQnhCVAo3l=zEzRoCRxQiLHiTvRgrNdvxZ=lwOlmFl8ABTEPpAQ=AGdICdIcQQRooOrhKEfbhLHcf0jL3Wj9W3awOKbEvcEr8E6ZAjpO/QfiLAa669Z7EDDwphYDI/Cm3Yhk0D2gHPW=XnDU=3kADeWhjZKKwN5sm/DGcDG7KiDD==',
        'Pragma': 'no-cache',
        'Referer': 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E9%2594%2580%25E5%2594%25AE%25E9%2583%25A8%25E7%25BB%258F%25E7%2590%2586,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'lang': 'c',
        'postchannel': '0000',
        'workyear': '99',
        'cotype': '99',
        'degreefrom': '99',
        'jobterm': '99',
        'companysize': '99',
        'ord_field': '0',
        'dibiaoid': '0',
        'line': '',
        'welfare': '',
        'type__1458': 'n4+xcD0DBDgDn07YG=D/iaReCq+BAIDmOSrD',
    }
    for page in range(1, 11):
        response = requests.get(
            f'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E9%2594%2580%25E5%2594%25AE%25E9%2583%25A8%25E7%25BB%258F%25E7%2590%2586,2,{page}.html',
            params=params,
            cookies=cookies,
            headers=headers
            # proxies = get_proxy()
        )
        engine_jds = response.json()['engine_jds']
        for jd in engine_jds:
            job_name = jd['job_name']
            updatedate = jd['updatedate']
            company_name = jd['company_name']
            providesalary_text = jd['providesalary_text']
            workarea_text = jd['workarea_text']
            attribute_text = ''.join(jd['attribute_text'])
            job_href = jd['job_href']
            describe = job_detail(job_href)
            print(job_href, page)
            job_list.append(
                [job_name, updatedate, company_name, providesalary_text, workarea_text, attribute_text, job_href,
                 describe])
            time.sleep(4)
            # break
        # break


if __name__ == '__main__':
    job_list = []
    get_info()
    df = pd.DataFrame(job_list)
    df.to_excel('数据分析师.xls')
