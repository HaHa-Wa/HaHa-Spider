import json

import requests

# 设置请求cookie
cookies = {
    'cna': 'df9DG+Ng12UCAS9k+SlYcMjX',
    'dnk': 'tb031723874',
    'sgcookie': 'E100ye%2BmgschiCeAv975qId7XO%2F%2Ba1YtMn5aC4B%2BM%2FE8X5lsMR2CH%2FkoKZ4IthJeAOxIzwNvgh%2BZq2bp1Gfe9gegUx%2BbRMH5VC8riM9N8iOdbmc%3D',
    'uc1': 'cookie14=UoeyBr7h5MpIag%3D%3D&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=UtASsssmeJpuuznauA%3D%3D&existShop=false&pas=0',
    'cancelledSubSites': 'empty',
    't': 'a8f206ab97b2e6d54ccad7a8b24e8d6e',
    'tracknick': 'tb031723874',
    'lid': 'tb031723874',
    'csg': '72b602c4',
    'enc': 'RBPpdX5kFx%2FmIh8IHBhhwim5Xsjgzkvz433GMtHZpRYI28CZPZCc6homb21Y31BWUuHfsU6Oh%2B1C42jTtRy6nw%3D%3D',
    '_tb_token_': 'e563b1b377ae8',
    'cookie2': '1608fc3d887a72c3dd902896caa42b17',
    'xlly_s': '1',
    'XSRF-TOKEN': 'bc715c96-4584-47ba-aa28-b1678945ec97',
    'JSESSIONID': '0DB3058E9BCED83EC409A901F1E9947D',
    'x5sec': '7b22617365727665723b32223a22376163313833353339623036656435656138303966636633363231363538343443494b7875707747454f4c5474724848714936463677456144444d354f5455334f4463314d5441374d6a44443234795742304144227d',
    'tfstk': 'cy0CBtmmUY3NmVYl-JOwUC2hnEUVZ0v_NHwEOpwb3eRwMSlCim_4hj0KqTazw51..',
    'l': 'fBS9xSamTmhuzRrWBOfZPurza77OjIRYIuPzaNbMi9fPOCCM5heNW65EUf8HCnhVFsNpR3kzvXKpBeYBcCqf8Hpf6xAZyVDmnmOk-Wf..',
    'isg': 'BEpKJz5yHQtoqJGk74X9HOfAmzbsO86Vq8Wp8tSD-R0oh-pBvMgppBz5lvNbT0Yt',
}

# 设置请求头 模拟浏览器请求
headers = {
    'authority': 'sjipiao.fliggy.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'cna=df9DG+Ng12UCAS9k+SlYcMjX; dnk=tb031723874; sgcookie=E100ye%2BmgschiCeAv975qId7XO%2F%2Ba1YtMn5aC4B%2BM%2FE8X5lsMR2CH%2FkoKZ4IthJeAOxIzwNvgh%2BZq2bp1Gfe9gegUx%2BbRMH5VC8riM9N8iOdbmc%3D; uc1=cookie14=UoeyBr7h5MpIag%3D%3D&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=UtASsssmeJpuuznauA%3D%3D&existShop=false&pas=0; cancelledSubSites=empty; t=a8f206ab97b2e6d54ccad7a8b24e8d6e; tracknick=tb031723874; lid=tb031723874; csg=72b602c4; enc=RBPpdX5kFx%2FmIh8IHBhhwim5Xsjgzkvz433GMtHZpRYI28CZPZCc6homb21Y31BWUuHfsU6Oh%2B1C42jTtRy6nw%3D%3D; _tb_token_=e563b1b377ae8; cookie2=1608fc3d887a72c3dd902896caa42b17; xlly_s=1; XSRF-TOKEN=bc715c96-4584-47ba-aa28-b1678945ec97; JSESSIONID=0DB3058E9BCED83EC409A901F1E9947D; x5sec=7b22617365727665723b32223a22376163313833353339623036656435656138303966636633363231363538343443494b7875707747454f4c5474724848714936463677456144444d354f5455334f4463314d5441374d6a44443234795742304144227d; tfstk=cy0CBtmmUY3NmVYl-JOwUC2hnEUVZ0v_NHwEOpwb3eRwMSlCim_4hj0KqTazw51..; l=fBS9xSamTmhuzRrWBOfZPurza77OjIRYIuPzaNbMi9fPOCCM5heNW65EUf8HCnhVFsNpR3kzvXKpBeYBcCqf8Hpf6xAZyVDmnmOk-Wf..; isg=BEpKJz5yHQtoqJGk74X9HOfAmzbsO86Vq8Wp8tSD-R0oh-pBvMgppBz5lvNbT0Yt',
    'pragma': 'no-cache',
    'referer': 'https://sjipiao.fliggy.com/flight_search_result.htm?searchBy=1280&ttid=seo.000000576&tripType=0&depCityName=%B9%E3%D6%DD&depCity=&arrCityName=%B9%F3%D1%F4&arrCity=&depDate=2022-12-17&arrDate=',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

# 设置请求参数
params = {
    '_ksTS': '1670289538876_173',
    'callback': 'jsonp174',
    'tripType': '0',
    'depCity': 'CAN',
    'depCityName': '广州',
    'arrCity': 'KWE',
    'arrCityName': '贵阳',
    'depDate': '2022-12-17',
    'searchSource': '99',
    'searchBy': '1280',
    'sKey': '',
    'qid': '',
    'needMemberPrice': 'true',
    '_input_charset': 'utf-8',
    'ua': '090#qCQXmTX2XunXPXi0XXXXXQkIOz07kG7+fwV7OFZ2AGBOzoxZhYmJGDd63oUlkURs3XQXiPR22amQXvXuCVHkRwiPwXQXagIPPzdf6/GAfPYiXXjPjXvfI/agsfXiXXdCVfR3PiM5/TQXU6hnXXa3HoQCh9T4ax73OJpeG2XXHYVySFhnLXa3HoSSh9k4XP73ISD5XvXQjsAKIX==',
    'itemId': '',
    'openCb': 'false',
}

# 发送请求 获取响应结果
response = requests.get('https://sjipiao.fliggy.com/searchow/search.htm', params=params, cookies=cookies,
                        headers=headers)
# 取出响应结果文本
ret = response.text
# 切割文本 将其处理为json可解析的文本
json_ret = ret[ret.find('(') + 1: -1]
# 将处理后的文本转换为json格式
json_ret = json.loads(json_ret)
# 取出返回结果中的数据
data = json_ret['data']
aircodeNameMap = data['aircodeNameMap']
airportMap = data['airportMap']
flight = data['flight']
# 循环取出机票信息
for info in flight:
    cabin = info['cabin']
    ticketPrice = cabin['ticketPrice']
    # 将折扣转换为float格式
    discount = cabin['discount'] / 10
    # 将机场代号进行转换
    airlineCode = airportMap[info['depAirport']]
    arrAirport = airportMap[info['arrAirport']]
    # 取出飞机起落时间
    arrTime = info['arrTime']
    depTime = info['depTime']
    buildPrice = info['buildPrice']
    # 打印机票信息
    print('起飞：', airlineCode, '落地：', arrAirport, '\n',
          '价格：', ticketPrice, '折扣：', discount, '\n',
          '起飞时间：',depTime,  '到达时间：', arrTime)
    print('-------------------------------------')
