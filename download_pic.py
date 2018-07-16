# coding=utf-8

import requests
from bs4 import BeautifulSoup
import json
import re

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

def download_pic(url):
    res = requests.get(url,headers = headers,stream = True).raw.read()
    # print(res.text)
    path = 'pic/'+ url[-13:]
    with open(path,'wb') as f1:
        res = f1.write(res)
        if res > 0:
            print(path+' down_load success')
    return 0

i_url = 'http://92zfl.com' #总地址
#
url = 'https://92zfl.com/luyilu/' #爬取地址

# url_add = ['','list_5_2','list_5_3','list_5_4','list_5_5','list_5_6','list_5_7','list_5_8','list_5_9','list_5_10',
#            'list_5_11','list_5_12', 'list_5_13', 'list_5_4', 'list_5_5', 'list_5_6', 'list_5_7', 'list_5_8', 'list_5_9', 'list_5_10']

url_add = ['']
for i in range(2,130):
    str1 = 'list_5_' + str(i)
    url_add.append(str1)

# print(url_add)

# src1 = 'https://www.images.zhaofulipic.com:8819/allimg'

# print(str2)


def get_html_luyi(url,i_url):
    list_html_luli = []

    res = requests.get(url, headers=headers)
    all_a = str(res.text)
    str2 = all_a.split(sep='"')

    for i in str2:
        if i.endswith('.html'):
            if 'luyilu' in i:
                i = i_url + i
                list_html_luli.append(i)
    return list_html_luli


def get_pic_html(url_pic_html):
    list_pic_html = []
    for i in url_pic_html:
        result2 = requests.get(i, headers=headers)
        result2 = str(result2.text)
        result2 = result2.split(sep = '"')
        for j in result2:
            if (j.endswith('.jpg') and j.startswith('https:')) and result2[result2.index(j)+1] == ' alt=':
                list_pic_html.append(j)
                # print(j)
                download_pic(j)
    return 0

# print(list_pic_site[0])

list_html_luli_exp = []
for i in url_add:
    if i == '':
        url = url
    else:
        url += i + '.html'
    # print(url)
    list_html_luli = get_html_luyi(url,i_url)
    # print(list_html_luli)
    list_html_luli_exp.extend(list_html_luli)
    url = 'https://92zfl.com/luyilu/'

# print(list_html_luli_exp)

import pandas as pd
df01 = pd.Series(list_html_luli_exp)
list_html_luli = list(df01.unique())
# print(list_html_luli)

def zengda(list_html_luli,num):
    new_html_lyli = []
    for i in range(len(list_html_luli)):
        new_html_lyli.append(list_html_luli[i])
        for k in range(2,num):
            str1 = list_html_luli[i][:-5] +'_' + str(k) + '.html'
            new_html_lyli.append(str1)
    return new_html_lyli

list_html_luli = zengda(list_html_luli,15)
# print(list_html_luli)


pic_url = get_pic_html(list_html_luli)
# print(pic_url)
'''
#
# for i in pic_url:
#     download_pic(i)

# import pandas as pd
# data1 = pd.read_csv('11.txt',header = None)
# # print(data1)
# data1 = list(data1.values)
# print(data1)

with open('11.txt','r') as f2:
    c = f2.read()

c = c.split('\n')
print(c)
print(type(c))
'''
# download_pic('https://www.images.zhaofulipic.com:8819/allimg/180707/151G63107-0.jpg')
# for i in c:
    # print(i)
    # download_pic(i)

