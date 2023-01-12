import requests
import json
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


def get_one(id):
    url = 'https://api.yunssss.com/kjh/2021-1/ec/public/api/exhibitor/getDetail?timestamp=1673426324147&nonce=B99oCcadsTLB5kKW&signature=77C266FF85A1C3AB8B78754BAF64F31B&channel=miniprogram&id=%s' % id
    ret = requests.get(url, headers=headers)
    res = json.loads(ret.content.decode())
    data = res['data']
    name = data['contactPerson']
    mobile = data['mobile']
    contactEmail = data['contactEmail']
    return [name, mobile, contactEmail]


def get_info():
    all_info = [['行业', '企业名称', '展位号', '联系人', '联系方式', '邮箱']]
    for page in range(1, 62):
        url = 'https://api.yunssss.com/kjh/2021-1/ec/public/api/exhibitor/getAll?timestamp=1673426277263&nonce=j8pFlZXJ3Dws4VAY&signature=8C7148B2A47669BD8B8494E624A38BE8&channel=miniprogram&size=20&page={0}&isHistory=false'.format(
            page)
        ret = requests.get(url, headers=headers)
        res = json.loads(ret.content.decode())
        data = res['data']['content']
        for x in data:
            exhibitionAreaName = x['exhibitionAreaName']
            exhibitionAreaBoothNumber = x['exhibitionAreaBoothNumber']
            shortName = x['shortName']
            id = x['id']
            name_list = get_one(id)
            info = [exhibitionAreaName, shortName, exhibitionAreaBoothNumber]
            info.extend(name_list)
            print(info)
            all_info.append(info)

    df = pd.DataFrame(all_info)
    df.to_excel('展位信息.xlsx')


if __name__ == '__main__':
    get_info()
