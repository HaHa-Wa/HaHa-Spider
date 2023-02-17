# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/16 5:47 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import requests
import pandas as pd


def main(sheng, shi, shi_id):
    cookies = {
        'SECKEY_ABVK': 'rNbX2TL8ad2TQbM3rMAZSBlJx/r9j6QxnyZ9xmjTHv4%3D',
        'BMAP_SECKEY': '8KXroISvloTqgakCp1zBTddBZeLiJSxMYTlYGt71PyEZFrHq9YmXjiPQ3xkTqwvHXYGu9gdamXA5lWj0jrrhMaD0fukBwWkaV_-qH_X-TxKMa6TNS9_IEJm__zqYWznZxbcjcLBwYYHRZmOedpdk-5bjfNEGt6jsW3HeUTuDQi6rSIwezIShPnyYIFlD0_Rg',
        'cookiesession1': '678A3E0E6BEB2796AC8288495631FB70',
        '_gid': 'GA1.2.1405142704.1676538146',
        '_cs_mk_ga': '0.5246022311878975_1676538146504',
        'reward': 'false',
        '__gaLOCC': 'GA1.2.910984230.1676538146',
        '__gaLOCC_gid': 'GA1.2.1860188382.1676538147',
        '_dc_gtm_UA-44069674-4': '1',
        '_ga_26ED7QQYK6': 'GS1.1.1676538146.1.0.1676538146.0.0.0',
        '_ga': 'GA1.1.910984230.1676538146',
        's': '66ecea9dc1e7ee9a546d463656fea311',
        'vary': '11d0f096be3cc722eae6187c56e85789312a35c2f6dcb0ad5286ac88f185d57d',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'SECKEY_ABVK=rNbX2TL8ad2TQbM3rMAZSBlJx/r9j6QxnyZ9xmjTHv4%3D; BMAP_SECKEY=8KXroISvloTqgakCp1zBTddBZeLiJSxMYTlYGt71PyEZFrHq9YmXjiPQ3xkTqwvHXYGu9gdamXA5lWj0jrrhMaD0fukBwWkaV_-qH_X-TxKMa6TNS9_IEJm__zqYWznZxbcjcLBwYYHRZmOedpdk-5bjfNEGt6jsW3HeUTuDQi6rSIwezIShPnyYIFlD0_Rg; cookiesession1=678A3E0E6BEB2796AC8288495631FB70; _gid=GA1.2.1405142704.1676538146; _cs_mk_ga=0.5246022311878975_1676538146504; reward=false; __gaLOCC=GA1.2.910984230.1676538146; __gaLOCC_gid=GA1.2.1860188382.1676538147; _dc_gtm_UA-44069674-4=1; _ga_26ED7QQYK6=GS1.1.1676538146.1.0.1676538146.0.0.0; _ga=GA1.1.910984230.1676538146; s=66ecea9dc1e7ee9a546d463656fea311; vary=11d0f096be3cc722eae6187c56e85789312a35c2f6dcb0ad5286ac88f185d57d',
        'Origin': 'https://m.loccitane.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://m.loccitane.cn/wap/gallery-storeList.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'city': shi_id,
    }

    response = requests.post('https://m.loccitane.cn/wap/tools-get_store_list.html', cookies=cookies, headers=headers,
                             data=data)
    ret = response.json()
    for haha in ret['data']:
        print(haha)
        store_name = haha['store_name']
        store_tel = haha['store_tel']
        store_addr = haha['store_addr']
        all_info.append([sheng, shi, store_name, store_addr, store_tel])


if __name__ == '__main__':
    all_info = [['省份', '城市', '店铺名', '店铺地址', '联系方式']]
    city_info = [
        {
            "name": "北京",
            "addr_id": "1",
            "child_index": "0",
            "children": [
                {
                    "name": "北京市",
                    "addr_id": "2",
                    "child_index": "0"
                }
            ]
        },
        {
            "name": "上海",
            "addr_id": "21",
            "child_index": "1",
            "children": [
                {
                    "name": "上海市",
                    "addr_id": "22",
                    "child_index": "1"
                }
            ]
        },
        {
            "name": "天津",
            "addr_id": "42",
            "child_index": "2",
            "children": [
                {
                    "name": "天津市",
                    "addr_id": "43",
                    "child_index": "2"
                }
            ]
        },
        {
            "name": "重庆",
            "addr_id": "62",
            "child_index": "3",
            "children": [
                {
                    "name": "重庆市",
                    "addr_id": "63",
                    "child_index": "3"
                }
            ]
        },
        {
            "name": "安徽",
            "addr_id": "104",
            "child_index": "4",
            "children": [
                {
                    "name": "合肥市",
                    "addr_id": "105",
                    "child_index": "4"
                },
                {
                    "name": "马鞍山市",
                    "addr_id": "195",
                    "child_index": "5"
                }
            ]
        },
        {
            "name": "福建",
            "addr_id": "227",
            "child_index": "5",
            "children": [
                {
                    "name": "福州市",
                    "addr_id": "228",
                    "child_index": "6"
                },
                {
                    "name": "厦门市",
                    "addr_id": "303",
                    "child_index": "7"
                }
            ]
        },
        {
            "name": "甘肃",
            "addr_id": "322",
            "child_index": "6",
            "children": [
                {
                    "name": "兰州市",
                    "addr_id": "323",
                    "child_index": "8"
                }
            ]
        },
        {
            "name": "广东",
            "addr_id": "423",
            "child_index": "7",
            "children": [
                {
                    "name": "广州市",
                    "addr_id": "424",
                    "child_index": "9"
                },
                {
                    "name": "东莞市",
                    "addr_id": "441",
                    "child_index": "10"
                },
                {
                    "name": "惠州市",
                    "addr_id": "455",
                    "child_index": "11"
                },
                {
                    "name": "深圳市",
                    "addr_id": "524",
                    "child_index": "12"
                }
            ]
        },
        {
            "name": "广西",
            "addr_id": "566",
            "child_index": "8",
            "children": [
                {
                    "name": "南宁市",
                    "addr_id": "567",
                    "child_index": "13"
                }
            ]
        },
        {
            "name": "贵州",
            "addr_id": "690",
            "child_index": "9",
            "children": [
                {
                    "name": "贵阳市",
                    "addr_id": "691",
                    "child_index": "14"
                }
            ]
        },
        {
            "name": "河北",
            "addr_id": "814",
            "child_index": "10",
            "children": [
                {
                    "name": "石家庄市",
                    "addr_id": "815",
                    "child_index": "15"
                },
                {
                    "name": "保定市",
                    "addr_id": "839",
                    "child_index": "16"
                },
                {
                    "name": "唐山市",
                    "addr_id": "945",
                    "child_index": "17"
                }
            ]
        },
        {
            "name": "河南",
            "addr_id": "998",
            "child_index": "11",
            "children": [
                {
                    "name": "郑州市",
                    "addr_id": "999",
                    "child_index": "18"
                },
                {
                    "name": "洛阳市",
                    "addr_id": "1052",
                    "child_index": "19"
                }
            ]
        },
        {
            "name": "黑龙江",
            "addr_id": "1176",
            "child_index": "12",
            "children": [
                {
                    "name": "哈尔滨市",
                    "addr_id": "1177",
                    "child_index": "20"
                }
            ]
        },
        {
            "name": "湖北",
            "addr_id": "1320",
            "child_index": "13",
            "children": [
                {
                    "name": "武汉市",
                    "addr_id": "1321",
                    "child_index": "21"
                },
                {
                    "name": "宜昌市",
                    "addr_id": "1422",
                    "child_index": "22"
                }
            ]
        },
        {
            "name": "湖南",
            "addr_id": "1436",
            "child_index": "14",
            "children": [
                {
                    "name": "长沙市",
                    "addr_id": "1437",
                    "child_index": "23"
                }
            ]
        },
        {
            "name": "吉林",
            "addr_id": "1573",
            "child_index": "15",
            "children": [
                {
                    "name": "长春市",
                    "addr_id": "1574",
                    "child_index": "24"
                },
                {
                    "name": "吉林市",
                    "addr_id": "1598",
                    "child_index": "25"
                }
            ]
        },
        {
            "name": "江苏",
            "addr_id": "1643",
            "child_index": "16",
            "children": [
                {
                    "name": "南京市",
                    "addr_id": "1644",
                    "child_index": "26"
                },
                {
                    "name": "常州市",
                    "addr_id": "1658",
                    "child_index": "27"
                },
                {
                    "name": "淮安市",
                    "addr_id": "1666",
                    "child_index": "28"
                },
                {
                    "name": "南通市",
                    "addr_id": "1683",
                    "child_index": "29"
                },
                {
                    "name": "苏州市",
                    "addr_id": "1692",
                    "child_index": "30"
                },
                {
                    "name": "泰州市",
                    "addr_id": "1710",
                    "child_index": "31"
                },
                {
                    "name": "无锡市",
                    "addr_id": "1717",
                    "child_index": "32"
                },
                {
                    "name": "徐州市",
                    "addr_id": "1726",
                    "child_index": "33"
                },
                {
                    "name": "盐城市",
                    "addr_id": "1738",
                    "child_index": "34"
                },
                {
                    "name": "扬州市",
                    "addr_id": "1748",
                    "child_index": "35"
                },
                {
                    "name": "镇江市",
                    "addr_id": "1756",
                    "child_index": "36"
                }
            ]
        },
        {
            "name": "江西",
            "addr_id": "1763",
            "child_index": "17",
            "children": [
                {
                    "name": "南昌市",
                    "addr_id": "1764",
                    "child_index": "37"
                }
            ]
        },
        {
            "name": "辽宁",
            "addr_id": "1874",
            "child_index": "18",
            "children": [
                {
                    "name": "沈阳市",
                    "addr_id": "1875",
                    "child_index": "38"
                },
                {
                    "name": "鞍山市",
                    "addr_id": "1889",
                    "child_index": "39"
                },
                {
                    "name": "大连市",
                    "addr_id": "1912",
                    "child_index": "40"
                }
            ]
        },
        {
            "name": "内蒙古",
            "addr_id": "1989",
            "child_index": "19",
            "children": [
                {
                    "name": "呼和浩特市",
                    "addr_id": "1990",
                    "child_index": "41"
                },
                {
                    "name": "包头市",
                    "addr_id": "2012",
                    "child_index": "42"
                }
            ]
        },
        {
            "name": "宁夏",
            "addr_id": "2103",
            "child_index": "20",
            "children": [
                {
                    "name": "银川市",
                    "addr_id": "2104",
                    "child_index": "43"
                }
            ]
        },
        {
            "name": "青海",
            "addr_id": "2130",
            "child_index": "21",
            "children": [
                {
                    "name": "西宁市",
                    "addr_id": "2131",
                    "child_index": "44"
                }
            ]
        },
        {
            "name": "山东",
            "addr_id": "2182",
            "child_index": "22",
            "children": [
                {
                    "name": "济南市",
                    "addr_id": "2183",
                    "child_index": "45"
                },
                {
                    "name": "德州市",
                    "addr_id": "2202",
                    "child_index": "46"
                },
                {
                    "name": "东营市",
                    "addr_id": "2214",
                    "child_index": "47"
                },
                {
                    "name": "济宁市",
                    "addr_id": "2230",
                    "child_index": "48"
                },
                {
                    "name": "青岛市",
                    "addr_id": "2268",
                    "child_index": "49"
                },
                {
                    "name": "威海市",
                    "addr_id": "2293",
                    "child_index": "50"
                },
                {
                    "name": "潍坊市",
                    "addr_id": "2298",
                    "child_index": "51"
                },
                {
                    "name": "烟台市",
                    "addr_id": "2311",
                    "child_index": "52"
                },
                {
                    "name": "淄博市",
                    "addr_id": "2331",
                    "child_index": "53"
                }
            ]
        },
        {
            "name": "山西",
            "addr_id": "2340",
            "child_index": "23",
            "children": [
                {
                    "name": "太原市",
                    "addr_id": "2341",
                    "child_index": "54"
                }
            ]
        },
        {
            "name": "陕西",
            "addr_id": "2471",
            "child_index": "24",
            "children": [
                {
                    "name": "西安市",
                    "addr_id": "2472",
                    "child_index": "55"
                },
                {
                    "name": "宝鸡市",
                    "addr_id": "2497",
                    "child_index": "56"
                }
            ]
        },
        {
            "name": "四川",
            "addr_id": "2589",
            "child_index": "25",
            "children": [
                {
                    "name": "成都市",
                    "addr_id": "2590",
                    "child_index": "57"
                },
                {
                    "name": "绵阳市",
                    "addr_id": "2722",
                    "child_index": "58"
                }
            ]
        },
        {
            "name": "新疆",
            "addr_id": "2873",
            "child_index": "26",
            "children": [
                {
                    "name": "乌鲁木齐市",
                    "addr_id": "2874",
                    "child_index": "59"
                }
            ]
        },
        {
            "name": "云南",
            "addr_id": "2987",
            "child_index": "27",
            "children": [
                {
                    "name": "昆明市",
                    "addr_id": "2988",
                    "child_index": "60"
                }
            ]
        },
        {
            "name": "浙江",
            "addr_id": "3133",
            "child_index": "28",
            "children": [
                {
                    "name": "杭州市",
                    "addr_id": "3134",
                    "child_index": "61"
                },
                {
                    "name": "湖州市",
                    "addr_id": "3148",
                    "child_index": "62"
                },
                {
                    "name": "嘉兴市",
                    "addr_id": "3154",
                    "child_index": "63"
                },
                {
                    "name": "金华市",
                    "addr_id": "3162",
                    "child_index": "64"
                },
                {
                    "name": "宁波市",
                    "addr_id": "3182",
                    "child_index": "65"
                },
                {
                    "name": "绍兴市",
                    "addr_id": "3201",
                    "child_index": "66"
                },
                {
                    "name": "温州市",
                    "addr_id": "3218",
                    "child_index": "67"
                },
                {
                    "name": "上虞市",
                    "addr_id": "3505"
                }
            ]
        }
    ]
    for x in city_info:
        print(x)
        sheng = x['name']
        print(sheng)
        for i in x['children']:
            shi = i['name']
            shi_id = i['addr_id']
            main(sheng, shi, shi_id)
    df = pd.DataFrame(all_info)
    # df.to_excel('weibo2.xlsx',index=False,options={'strings_to_urls': False})
    with pd.ExcelWriter('店铺信息.xlsx', engine='xlsxwriter', options={'strings_to_urls': False}) as writer:
        df.to_excel(writer, index=False)
