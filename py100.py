#coding=utf-8

import requests
from bs4 import BeautifulSoup
# import lxml

'''
    1,明确需求
        爬去python100例题
            标题
            题目
            程序分析
            源代码
    2，分析源码
        入口地址：
        1，获取100道题的a连接
        2.分析请求这个100个链接对应页面
    3，代码实现
'''

startUrl = 'http://www.runoob.com/python/python-100-examples.html'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

response = requests.get(startUrl, headers = headers).content.decode('utf-8')

# 解析 文档
soup = BeautifulSoup(response, 'lxml')
# # 提取1个a链接
# soup1 = soup.find(id = 'contend').ul.li.find('a')
# # print(soup1)
# 提取100个a链接
soup1 = soup.find(id = 'content').ul.li.find_all('a')
# print(soup1)
link = []
for i in soup1:
    link.append(i['href'])
# 请求100个a连列
num = 1
for l in link:
    # print(l)

    url_head = 'http://www.runoob.com'
    result = requests.get(url_head + l,headers = headers).content.decode('utf-8')

    # 继续解析源代码
    html = BeautifulSoup(result,'lxml')
    # print(html)

    # 提取内容
    content = {}
    # 标题
    content['title'] = html.find(id = 'content').h1.string #不含子目录的文本
    # 题目
    content['题目'] = html.find(id = 'content').find_all('p')[1].text #含字目录find_all('p')
    # 程序分析
    content['程序分析'] = html.find(id = 'content').find_all('p')[2].text
    # 源代码
    try:
        content['code'] = html.find(class_ = 'hl-main').text
    except:
        content['code'] = html.find('pre').text  # 含字目录find_all('p')

    # 保存文件
    with open('py100.txt','a+',encoding= 'utf-8') as file:
        file.write(content['title']+ '\n')
        file.write(content['题目'] + '\n')
        file.write(content['程序分析'] + '\n')
        file.write(content['code'] + '\n')
        file.write('='*40 + '\n')

    print('第%d下载完成' % num)
    num += 1

# w3cschool

## CSS选择器
# 1.通过标签名进行查找，及如果保存在列表当中
tag_a = result.select('a')
# 等同于
result.find_all('a')

# 2.通过类名查找
result.select('.left') #都是保存在列表当中
# 等同于
result.find(class_ = 'left')

# 3.通过id名查找
result.select('#menu')
result.dinf(id = 'menu')

# 等价关系
#  #content  <===>  id = 'content'
#  .left     <===>  class = 'left

# 4.通过属性查找
# 通过 a 标签中的属性 aa 来查找
result.select('a[name = "aa"')
result.find(name = 'a',attrs  = {'name':"aa"})

# 5.组合查找
# id为content中找一个class为left 中的 a 标签
result.select('#content .left a') #空格表示这个id里面的一个东西
result.find(id = 'content').find(class_ = 'left').find_all('a')

# 6.获取文本get_text()
result.select('a[name="aa"]')[0].get_text()
result.select('a[name="aa"]')[0].text

# 7.获取属性
result.select('a[name="aa"]')[0]['href']
result.select('a[name="aa"]')[0].attrs['href']

# </br>是换行的标签的意思

## 修改为select
# 提取100个a链接
soup1 = soup.select('#content ul li a')#.ul.li.find_all('a')
# print(soup1)
link = []
for i in soup1:
    link.append(i['href'])
# 请求100个a连列
# print(link)
num = 1

for l in link:
    # print(l)

    url_head = 'http://www.runoob.com'
    result = requests.get(url_head + l,headers = headers).content.decode('utf-8')

    # 继续解析源代码
    html = BeautifulSoup(result,'lxml')
    # print(html)

    # 提取内容
    content = {}
    # 标题
    content['title'] = html.select('#content h1')[0].text #不含子目录的文本
    # 题目
    content['题目'] = html.select('#content p')[1].text #含字目录find_all('p')
    # 程序分析
    content['程序分析'] = html.select('#content p')[2].text
    # 源代码
    try:
        content['code'] = html.select('.hl-main')[0].text
    except:
        content['code'] = html.select('pre')[0].text  # 含字目录find_all('p')

    # 保存文件
    with open('py100.txt','a+',encoding= 'utf-8') as file:
        file.write(content['title']+ '\n')
        file.write(content['题目'] + '\n')
        file.write(content['程序分析'] + '\n')
        file.write(content['code'] + '\n')
        file.write('='*40 + '\n')

    print('第%d下载完成' % num)
    num += 1

## lxml用法
from lxml import etree

# 创建lxml对象。允许标签有错
html = etree.HTML(open('web.html',encoding = 'utf-8').read())
# print(html) 是一个element

# 将lxml 对象字符串序列化
result = etree.tostring(html, pretty_print= True,encoding= 'utf-8').decode('utf-8')
# print(result)

html = etree.fromstring(open('web.html',encoding = 'utf-8').read())

# 标准很严格，标签不允许有错，
html = etree.parse(open('web.html',encoding = 'utf-8').read())

# 选取节点,可以在浏览器其中边写边看是否找的对
#  // 从全文当中查找
html.xpath('//div')

#  / 表示从根节点开始查找
html.xpath('/html/body/div')

#  从全文中查找div，并将其下面的 a 标签找出来
html.xpath('//div/a')

#
html.xpath('//div/a/..') #查找该节的父节点
html.xpath('//div/a/.') #该节点自己

# 查找属性
# [@class = 'xxx']
# 下标获取某个元素
html.xpath('//div[@id="menu"]/a')[0]

# 里面的第几个东西
html.xpath('//div[@id="menu"]/a[1]')

# 获取最后一个元素
html.xpath('//div[@id="menu"]/a[last()]')

# 前面3个
html.xpath('//div[@id="menu"]/a[position()<3]')

#
html.xpath('//div[@id="menu"]/a[span="haha"]')

# *表示认识标签
html.xpath('//*[@id="menu"]/a[span = "haha"]')

# 或者的意思
html.xpath('//*[@id="menu"]/a[span = "haha" | //div[@class="left"]/a[1]')

# 加减乘除的运算
html.xpath('//*[@id="menu"]/a[span =50 ] + //*[@id="menu"]/a[span =50 ]')