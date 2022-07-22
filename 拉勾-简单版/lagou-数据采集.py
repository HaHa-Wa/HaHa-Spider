import requests
import tablib
import xlwt
import time


def processing_data(content_list):
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    # 写入excel
    for i, content in enumerate(content_list):
        for x, info in enumerate(content):
            worksheet.write(i, x, label=info)  # 将数据存入excel
    # 保存
    workbook.save(keyWord + '.xls')


def parse_list(jobList):
    for job in jobList:
        all_job.append([job['positionName'], job['jobNature'], job['education'], job['salary'], job['salaryMonth'],
                        job['workYear'], job['positionAdvantage'], job['positionDetail'], job['linestaion'], job['firstType'], job['companySize'],
                        job['companyShortName'], "".join(job['companyLabelList'])])


def main():
    cookies = {
        'user_trace_token': '20220323220821-7d0e1f1f-a3fc-4ab3-8b91-a85020884e16',
        '_ga': 'GA1.2.315042611.1648044502',
        'JSESSIONID': 'ABAAAECAAEBABIID1076941F36C603C049C69CDB6F27009',
        'WEBTJ-ID': '20220323220837-17fb71ba99adb2-0990a4f31e1fca-133a645d-2007040-17fb71ba99b1b3',
        'RECOMMEND_TIP': 'true',
        'LGUID': '20220323220838-48d6f3f1-7c98-48d2-989d-942f210affd9',
        'privacyPolicyPopup': 'false',
        'sajssdk_2015_cross_new_user': '1',
        'sensorsdata2015session': '%7B%7D',
        '__lg_stoken__': '49966733fd5589dab4aa538fa47037bf85b527e4a5f3130ba4d6278aa68a66fb70f56ac344d799436f0b5d1b6cacfc13d4337a3c1f912c1291b4954c8ac04b9749c66618c19a',
        'X_MIDDLE_TOKEN': '3a49dd58c6aa9a078985e46c2d778f83',
        'gate_login_token': 'dc9f9e2c2d1a9a24ca72c1caafab032291af036444e5fbf32fae02a6014ab28f',
        'LG_LOGIN_USER_ID': '781ad27dc7889a9fd3f7acd71bbe73c85a4ccfeeb10fbbad4bacf5361c4be947',
        'LG_HAS_LOGIN': '1',
        '_putrc': '6C0134276AACF97B123F89F2B170EADC',
        'login': 'true',
        'unick': '%E5%91%A8%E6%99%A8%E9%98%B3',
        'showExpriedIndex': '1',
        'showExpriedCompanyHome': '1',
        'showExpriedMyPublish': '1',
        'hasDeliver': '0',
        'index_location_city': '%E4%B8%8A%E6%B5%B7',
        'PRE_UTM': '',
        'PRE_HOST': '',
        'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
        'LGSID': '20220323233136-c07c52f1-0f00-42aa-85d6-d0bb535a7fda',
        'PRE_SITE': 'https%3A%2F%2Fwww.lagou.com',
        '_gat': '1',
        '__SAFETY_CLOSE_TIME__17454876': '1',
        'TG-TRACK-CODE': 'index_search',
        'SEARCH_ID': '84e0f216cefc43d0a7efecc4f6e53d52',
        'X_HTTP_TOKEN': 'c3dcc230cd9a1c7e6059408461459279957786d7ea',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2217454876%22%2C%22first_id%22%3A%2217fb71bada98e1-0ed0ae6e67a42c-133a645d-2007040-17fb71badaaa38%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2299.0.4844.74%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217fb71bada98e1-0ed0ae6e67a42c-133a645d-2007040-17fb71badaaa38%22%7D',
        'LGRID': '20220323233147-a5489af5-ba52-49da-a7fa-f2e96ff3ecf7',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'x-anit-forge-code': '0',
        'traceparent': '00-a30ce85c046da52a7d456a2e01e29c26-f4a907b4d63e19cf-01',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'x-anit-forge-token': 'None',
        'sec-ch-ua-platform': '"macOS"',
        'Origin': 'https://www.lagou.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%96%B0%E5%AA%92%E4%BD%93/p-city_215?&cl=false&fromSearch=true&labelWords=&suginput=',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    params = (
        ('city', '深圳'),
        ('needAddtionalResult', 'false'),
    )
    for x in range(1, 27):
        data = {
            'first': 'true',
            'pn': str(x),
            'kd': keyWord
        }

        response = requests.post('https://www.lagou.com/jobs/positionAjax.json', headers=headers, params=params,
                                 cookies=cookies, data=data)
        result = response.json()['content']['positionResult']['result']
        parse_list(result)
        time.sleep(2)
        print(x)


if __name__ == '__main__':
    keyWord = '新媒体'
    all_job = []
    main()
    processing_data(all_job)
