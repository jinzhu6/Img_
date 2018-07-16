#coding=utf-8
import requests
import time
import json
import re

startUrl = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8' \
      '&word={0}' \
      '&oq={0}&rsp=-1'

# keyword = input('输入搜索的关键字：')
keyword = '简约'
response = requests.get(startUrl.format(keyword)).content.decode('utf-8','ignore')
# print(response)

# 滚动触发的事件第一个
rollUrl = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result' \
      '&queryWord={0}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0' \
      '&word={0}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=' \
      '&pn={1}&rn=30' \
      '&gsm={2}' \
      '&{3}='

# 滚动触发的事件第二个
# url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%AE%80%E7%BA%A6&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E7%AE%80%E7%BA%A6&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=60&rn=30&gsm=3c&1531665949548='

'''
第一个触发的参数
pn: 30
gsm: 1e
1531665949468: 
第二个触发的参数
pn: 60
gsm: 3c
1531665949548: 这个就是时间戳 
1531666486.058488
1531666520921
'''

# 设定参数
pn = 30
gsm = hex(pn)[-2:]
# print(gsm)
rt = int(time.time()*1000)
# print(rt)

roll = 1
while True:
      response = requests.get(rollUrl.format(keyword,pn,gsm,rt)).content.decode('utf-8','ignore')
      response = json.loads(response)
      listNum = response['listNum']
      displayNum = response['displayNum']
      data = response['data']

      print('第{0}次滚动'.format(roll))

      for i in data:
            if i:
                  # 获取图片的下载地址和文件名
                  middleUrl = i['middleURL']
                  fromPageTitleEnc = i['fromPageTitleEnc']
                  pattern = re.compile("[\\\/\*:\?\"<>|\.]")
                  fromPageTitleEnc = pattern.sub('_',fromPageTitleEnc)
                  # print('filename:',fromPageTitleEnc)

                  image = requests.get(middleUrl,stream = True).raw.read()
                  with open('baidu_pic/'+ fromPageTitleEnc + '.jpg','wb') as file:
                        file.write(image)

                  print(fromPageTitleEnc,'downloaded')

      if listNum < displayNum:
            pn += 30
            gsm = hex(pn)[-2:]
            rt = int(time.time() * 1000)
            roll += 1
      else:
            break

