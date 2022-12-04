import requests
import pandas as pd
from retrying import retry


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def get_info(params, cookies, headers, data):
    response = requests.post(
        'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    return response


def main(c_id):
    comment_list = [['userNickName', 'mark', 'gmtModified', 'agreeCount', 'termId', 'id', 'content']]
    cookies = {
        'NTESSTUDYSI': '5e046a9db7c24defb130f51f5b85cbcf',
        'EDUWEBDEVICE': 'fce2a9e03c624c12860ef37cf6aa1276',
        'Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b': '1670054911',
        'hb_MA-A976-948FFA05E931_source': 'www.google.com',
        'WM_TID': 'n%2BowxSY5ULVFAARUQBKFYaY6AG%2BJWnS4',
        '__yadk_uid': 'GI5k9b4w9HW3pocMFcC598xixPJS6be1',
        'WM_NI': 'UgV5P4Qyi13SLA7LASK6clb0jNqqzlQ2DnEs7rEnJ%2BfIVE7Iv8cLrtVJFHb93gWw3v6wi4LsPqq%2FCiqyCZ11KD%2FEui3DP6aetpOdT6oGUUvHLn9WFnyDXbVx6R5yy4XCZjg%3D',
        'WM_NIKE': '9ca17ae2e6ffcda170e2e6ee82c17fa8ae87acb246a6e78ea6d85e879b8bacc552a39584d2cc34f3ada4b1d72af0fea7c3b92a97b99ad6d34093a7a7d2b259909ff9adc45989eaad8de13caa92bf92f96893ee8c8fc879f5ae8b8fc921a6979aa6b643b6e8adadf18096968aa9e133f1b99998b27ef6a9a7d5cf7994afbfd0c263b3a78dbbb43b899ce1a6f863f19ca0d7e46fb8b08185d73ead999bb6f54490b2f7b8c566bb9c9883d574f68efb9afc409c9d968be637e2a3',
        'Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b': '1670145160',
    }

    headers = {
        'authority': 'www.icourse163.org',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'NTESSTUDYSI=5e046a9db7c24defb130f51f5b85cbcf; EDUWEBDEVICE=fce2a9e03c624c12860ef37cf6aa1276; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1670054911; hb_MA-A976-948FFA05E931_source=www.google.com; WM_TID=n%2BowxSY5ULVFAARUQBKFYaY6AG%2BJWnS4; __yadk_uid=GI5k9b4w9HW3pocMFcC598xixPJS6be1; WM_NI=UgV5P4Qyi13SLA7LASK6clb0jNqqzlQ2DnEs7rEnJ%2BfIVE7Iv8cLrtVJFHb93gWw3v6wi4LsPqq%2FCiqyCZ11KD%2FEui3DP6aetpOdT6oGUUvHLn9WFnyDXbVx6R5yy4XCZjg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee82c17fa8ae87acb246a6e78ea6d85e879b8bacc552a39584d2cc34f3ada4b1d72af0fea7c3b92a97b99ad6d34093a7a7d2b259909ff9adc45989eaad8de13caa92bf92f96893ee8c8fc879f5ae8b8fc921a6979aa6b643b6e8adadf18096968aa9e133f1b99998b27ef6a9a7d5cf7994afbfd0c263b3a78dbbb43b899ce1a6f863f19ca0d7e46fb8b08185d73ead999bb6f54490b2f7b8c566bb9c9883d574f68efb9afc409c9d968be637e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1670145160',
        'origin': 'https://www.icourse163.org',
        'pragma': 'no-cache',
        'referer': 'https://www.icourse163.org/course/SYSU-20016',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    params = {
        'csrfKey': '5e046a9db7c24defb130f51f5b85cbcf',
    }
    page = 1
    num_data = 0
    while True:
        data = {
            'courseId': c_id,
            'pageIndex': page,
            'pageSize': '20',
            'orderBy': '3',
        }

        response = get_info(params=params,
                            cookies=cookies,
                            headers=headers,
                            data=data,
                            )
        data = response.json()['result']
        data_list = data['list']
        totleCount = data['query']['totleCount']
        for co in data_list:
            content = co['content']
            userNickName = co['userNickName']
            mark = co['mark']
            gmtModified = co['gmtModified']
            agreeCount = co['agreeCount']
            termId = co['termId']
            id = co['id']
            comment_list.append([userNickName, mark, gmtModified, agreeCount, termId, id, content])
        num_data += len(data_list)

        if num_data == int(totleCount):
            break
        page += 1
    df = pd.DataFrame(comment_list)
    df.to_excel(f'comment/{c_id}.xls')


if __name__ == '__main__':
    df = pd.read_excel('课程.xls')
    print(df)
    for c_id in df[1]:
        print(c_id)
        # c_id = 20016
        main(c_id)
