#coding=utf-8

import requests

from lxml import etree

import time

'''
    1,需求分析
        获取详细的招聘内容
            职位名称，职位，人数，时间
                入口地址
    2，源码分析
        获取所有的行的数据 //tr[@class='even']|//tr[@class='odd']
        职位：//tr[@class='even']|//tr[@class='odd']/td[1]
        人数：//tr[@class='even']|//tr[@class='odd']/td[2]
        时间：//tr[@class='even']|//tr[@class='odd']/td[3]
        地点：//tr[@class='even']|//tr[@class='odd']/td[4]
        类别：//tr[@class='even']|//tr[@class='odd']/td[5]/text()
        下一页的：//a[@id='next']/@href    
    3，代码实现
'''

startUrl='https://hr.tencent.com/position.php'

'''
    一，入口地址
'''
# 身份信息
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

response = requests.get(startUrl,headers = headers).text

# print(response)

'''
    二，提取内容
'''
# 解析源码
html = etree.HTML(response)

page = 1
while True:
    # 获取所有行
    tr = html.xpath("//tr[@class='even']| //tr[@class='odd']")

    # 获取下一页
    nextPage = html.xpath("//a[@id='next']/@href")

    # 遍历获取每一行内容
    jobDic = {}

    num = 1
    for i in tr:
        jobDic['title'] = i.xpath("string(td[1])")
        jobDic['type'] = i.xpath("string(td[2])")
        jobDic['num'] = i.xpath("string(td[3])")
        jobDic['address'] = i.xpath("string(td[4])")
        jobDic['date'] = i.xpath("string(td[5])")

        # print(jobDic)
        print('第{0}页第{1}条信息'.format(page,num))
        num += 1

        # 防止速度过快
        time.sleep(0.5)

        # 保存信息
        # ..表示上一层
        with open('../../jupyter_file/tencent.txt','a+',encoding= 'utf-8') as file:
            file.write(jobDic['title'] + '::')
            file.write(jobDic['type'] + '::')
            file.write(jobDic['num'] + '::')
            file.write(jobDic['address'] + '::')
            file.write(jobDic['date'] + '\n')


    # 翻页获取下一页地址
    if nextPage[0] == 'javascript:;':
        break
    else:
        startUrl = 'https://ht.tencent.com'+ nextPage[0]
        page += 1





