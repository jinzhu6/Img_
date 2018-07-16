#coding=utf-8

import requests

from lxml import etree

import re

import json

'''
    1.需求分析
        title,gsmc,gz,add,jy,xl,fuli
        入口地址：https://www.zhaopin.com/        
    2.源码分析
        所有职位分类标签：//div[@class='zp-jobNavigater-pop-list']/a
        职位详细列表：https://sou.zhaopin.com/?jl=489kw=写标签就行            
    3，代码实现
'''

headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

startUrl = 'https://www.zhaopin.com/'
# info_url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=538&workExperience=0103&education=4&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&lastUrlQuery=%7B%22jl%22:%22538%22,%22we%22:%220103%22,%22el%22:%224%22,%22kw%22:%22%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%22,%22kt%22:%223%22%7D'
# info_url = 'https://fe-api.zhaopin.com/c/i/sou?start={0}&pageSize=60' \
#            '&cityId=538&workExperience=-1&education=-1&companyType=-1' \
#            '&employmentType=-1&jobWelfareTag=-1&kw={1}&kt=3' \
#            '&lastUrlQuery=%7B%22p%22:2,%22jl%22:%22538%22,%22kw%22:%22%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%22,%22kt%22:%223%22%7D'

# 1.获取职位标签
def get_job_tag(startUrl):
    '''
        一。请求首页
    '''

    response = requests.get(startUrl).text

    # print(response)

    # 解析源码
    html = etree.HTML(response)

    # 获取所有的职位分类标签
    job_type = html.xpath("//div[@class='zp-jobNavigater-pop-list']/a/text()")

    return job_type

# 2.获取职位信息
def get_job_info(info_url,kw, start=0 ):
    info_response = requests.get(info_url.format(start,kw) , headers=headers)

    # print(info_response)

    # 解析详情页面,动态页面是不需要解析的，直接json()就可以的
    info_html = info_response.json()

    # print(info_html['data'])

    print('-----------------')

    job_Dic = {}

    for i in info_html['data']['results']:
        job_Dic['city'] = i['city']['items'][0]['name']
        job_Dic['companyName'] = i['company']['name']
        job_Dic['companySize'] = i['company']['size']['name']
        job_Dic['companyType'] = i['company']['type']['name']
        job_Dic['eduLevel'] = i['eduLevel']['name']
        job_Dic['jobName'] = i['jobName']
        job_Dic['jobType'] = i['jobType']['display']
        job_Dic['salary'] = i['salary']
        job_Dic['updateDate'] = i['updateDate']
        job_Dic['workingExp'] = i['workingExp']['name']
        job_Dic['welfare'] = i['welfare']

        # print(job_Dic)

        # 保存数据
        if unique_data(job_Dic):
            jod_Dic = clearn_data(job_Dic)
            save_data(job_Dic)

    return info_html['data']['numFound']

# 过滤重复数据
companyList = []
jobNameList = []
def unique_data(data):
    if (data['jobName'] in jobNameList) and (data['companyName'] in companyList):
        return False
    else:
        companyList.append(data['companyName'])
        companyList.append(data['jobName'])
        return True

# 数据清洗
def clearn_data(data):
    data['welfare'] = '/'.join([str(i) for i in data['welfare']])

    data['companySize'] = data['companySize'].strip('人')

    pattern = re.compile("[\d]+")
    strs = pattern.findall(data['workingExp'])
    data['workingExp'] = '-'.join([str(i) for i in strs])

    # 处理掉小数点
    data['salary'] = re.sub('K', '000', data['salary'])

    s1 = data['salary'].split('-')

    s3 = []
    for ss in s1:
        if '.' in ss:
            s2 = ss.split('.')
            # print(s2)
            s3.append(s2[0]+s2[1][:-1])
            # ss = s3
            # print(ss)
        else:
            s3.append(ss)
        data['salary'] = '-'.join([i for i in s3])

    return data

# 保存数据
def save_data(data):
    data = '::'.join([str(i) for i in data.values()])
    print(data)

    with open('zlzp.txt','a+',encoding= 'utf-8') as file:
        file.write(data + '\n')


# https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&kt=3&lastUrlQuery=%7B%22jl%22:%22538%22,%22kw%22:%22%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%22,%22kt%22:%223%22%7D

# https://fe-api.zhaopin.com/c/i/sou?start={0}&pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={2}&kt=3&lastUrlQuery=%7B%22p%22:2,%22jl%22:%22538%22,%22kw%22:%22%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%22,%22kt%22:%223%22%7D



if __name__ == '__main__':
    start = 0
    page = 1
    while True:
        infoUrl = 'https://fe-api.zhaopin.com/c/i/sou?start={0}&pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1' \
                  '&employmentType=-1&jobWelfareTag=-1&kw={1}&kt=3' \
                  '&lastUrlQuery=%7B%22p%22:2,%22jl%22:%22538%22,%22kw%22:%22%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%22,%22kt%22:%223%22%7D'

        # 先获取只为列表
        kw = get_job_tag(startUrl)
        print(kw[14])
        # 在获取每一页的详细情况
        get_job_info(infoUrl, kw[14])

        # 获取当前页面的条数
        numFound = get_job_info(infoUrl,kw[14])

        print('第{0}页'.format(page))

        if start < numFound:
            start += 60
            page += 1
        else:
            print('爬完了')
            break



# print(job_type)

''' 
    获取职位的详细列表页面


# 这边的网页是动态加载的，需要在这个位置才能找的到
info_url = 'https://sou.zhaopin.com/?jl=489kw={0}&tk=3'
info_url = 'https://fe-api.zhaopin.com/c/i/sou?' \
        'start={0}
           'pageSize=60' \
           '&cityId=538' \
           '&workExperience=0103' \
           '&education=4' \
           '&companyType=-1' \
           '&employmentType=-1' \
           '&jobWelfareTag=-1' \
           '&kw={1}kt=3' \
           '&lastUrlQuery=%7B%22jl%22:%22538%22,' \
           '%22we%22:%220103%22,' \
           '%22el%22:%224%22,' \
           '%22kw%22:%22%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%22,' \
           '%22kt%22:%223%22%7D'

info_response = requests.get(info_url.format(job_type[7]),headers = headers).text

# print(info_response)

# 解析详情页面
info_html= etree(info_response)

job_title = info_html.xpath("//span[@class='job_title']/text()")
print(job_title)
'''