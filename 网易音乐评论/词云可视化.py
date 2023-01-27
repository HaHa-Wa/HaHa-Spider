# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/14 2:52 下午
@Auth ： HaHa-Wa
@File ：词云可视化.py
@IDE ：PyCharm
"""
import matplotlib.pyplot as plt  # 数据可视化
import jieba  # 词语切割
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS  # 词云，颜色生成器，停止词
import numpy as np  # 科学计算
from PIL import Image  # 处理图片
import pandas as pd

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


# 读取停词表
def read_stopword_file():
    with open('baidu_stopwords.txt', 'r+') as f:
        stopwords = f.read()
    return stopwords.split('\n')


# 读取数据
def read_excel():
    df = pd.read_excel('%s.xlsx'%file_name)
    return df


# 绘制词云
def paint_wordcloud(stopwords, space_list):
    backgroud = np.array(Image.open('pkq.jpeg'))

    wc = WordCloud(width=1400, height=2200,
                   background_color='white',
                   mode='RGB',
                   mask=backgroud,  # 添加蒙版，生成指定形状的词云，并且词云图的颜色可从蒙版里提取
                   max_words=500,
                   stopwords=stopwords,  # 内置的屏蔽词,并添加自己设置的词语
                   # font_path='C:\Windows\Fonts\STZHONGS.ttf',
                   max_font_size=150,
                   relative_scaling=0.6,  # 设置字体大小与词频的关联程度为0.4
                   random_state=50,
                   scale=2,
                   font_path='/System/Library/Fonts/Hiragino Sans GB.ttc'
                   ).generate(space_list)

    image_color = ImageColorGenerator(backgroud)  # 设置生成词云的颜色，如去掉这两行则字体为默认颜色
    wc.recolor(color_func=image_color)

    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭x,y轴
    plt.show()  # 显示
    wc.to_file('%s.png' % file_name)  # 保存词云图


# 主函数
def ciyun(textfile):
    stopwords = STOPWORDS
    baidu_stopwords = read_stopword_file()
    stopwords.update(baidu_stopwords)
    wordlist = jieba.lcut(textfile)  # 切割词语
    # print(wordlist)
    word_ = {}
    # 统计词频 排除停用词
    for word in wordlist:
        if word.strip() not in baidu_stopwords:
            if len(word) > 1:
                if word != '\t':
                    if word != '\r\n':
                        # 计算词频
                        if word in word_:
                            word_[word] += 1
                        else:
                            word_[word] = 1
    # 进行降序排列
    sorted_wordlist = sorted(word_.items(), key=lambda i: (i[1], i[0]), reverse=True)
    print(sorted_wordlist[0:50])
    # 绘制词云
    space_list = ' '.join(wordlist)  # 空格链接词语
    paint_wordcloud(stopwords, space_list)
    # 绘制柱状图


# 统计文本函数
def statistics_text(data):
    text = ""
    for item in data[1]:
        print(item)
        try:
            text += item.replace('\n', '')
        except:
            continue
        # break
    return text


def main():
    df = read_excel()
    wenben = statistics_text(df)
    ciyun(wenben)


if __name__ == '__main__':
    file_name = '孤勇者'
    main()
    read_excel()
