import pandas as pd
import pdfplumber as pdfplumber
import requests


def dowload_pdf(file_name, url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    ret = requests.get(url, headers=headers)
    with open(f'{file_name}.pdf', 'wb') as f:
        f.write(ret.content)


def parse_pdf(file_name):
    pdf = pdfplumber.open(f"{file_name}.pdf")
    p0 = pdf.pages[16]
    # p1 = pdf.pages[31]
    print(p0)
    table = p0.extract_table()
    # table1 = p1.extract_table()
    print(table)
    df1 = pd.DataFrame(table[1:], columns=table[0])
    print(df1)
    # df2 = pd.DataFrame(table1[1:], columns=table[0])
    # df_all = pd.concat([df1, df2])

    # print(df_all)
    # df_all.to_csv('2014.csv')


if __name__ == '__main__':
    # url = 'https://wwwoa.ipe.org.cn//Upload/202211030232584873.pdf'
    # dowload_pdf('2022', url)
    file_name = '2015'
    parse_pdf(file_name)
