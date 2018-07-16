#coding=utf-8
'''
    1.需求分析
        1.获取帖子标题
        2.帖子的相关内容
    2.源码分析
        入口：https://www.cblogs.com
        获取帖子链接  //div[@class='post_item_body']/h3/a/@href
        获取下一页的文本  //div[@class='pager']/a[last()/text()]
        获取下一页的herf属性  //div[@class='pager']/a[last()]/@href
        对每一篇帖子标题匹配  //*[@id='cb_post_title_url']
        帖子所有文本内容  string(//*[@id='cnblogs_post_body'])
    3.代码实现
'''
# xpath序号从1开始，里面没有子节点使用text()获取文本
# //div[@class='pager']/a[1]/text()
# 有子节点的情况下，获取所有文本
# string(//div[@class='pager'])

'''
               bs4     lxml
 没有子节点有    string  text()
 有子节点有     text    string()
'''

# 获取属性href
# //div[@class='pager']/a[1]/@href

import requests
from lxml import etree

# 1.发送请求获取首页帖子
startUrl = 'https://www.cnblogs.com'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

page = 1

while True:

    response = requests.get(startUrl,headers = headers).text

    # print(response)

    # 解析源码
    html = etree.HTML(response)

    # 获取帖子的url
    href = html.xpath("//div[@class='post_item_body']/h3/a/@href")
    # print(href)

    # 获取下一页的文本及url
    next_page = html.xpath("//div[@class='pager']/a[last()]/text()")
    # print(next_page)
    next_page_url = html.xpath("//div[@class='pager']/a[last()]/@href")
    print(next_page_url)

    # 2。获取每一篇帖子内容及标题
    num = 1

    for i in href:
        result = requests.get(i,headers = headers).text
        # print(result)
        # 解析源码
        contents = etree.HTML(result)
        # 提取帖子标题
        title = contents.xpath("//*[@id='cb_post_title_url']/text()")
        print(title)
        # 提取详情内容
        info = contents.xpath("string(//*[@id='cnblogs_post_body'])")
        # print(info)
    #     print()

    # 3.保存内容
        with open('cnblogs.txt','a+',encoding= 'utf-8') as file:
            file.write('['+ title[0] + ']'+ '\n')
            file.write(info + '\n')
            file.write('='*80 + '\n')

        print('第{}页第{}篇帖子'.format(page,num))
        num += 1

    if next_page[0] == 'Next >':
        startUrl = 'https://www.cnblogs.com' + next_page_url[0]
        page += 1

    else:
        break