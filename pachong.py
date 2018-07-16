import requests

result = requests.get('http://www.beifeng.com')
# 数据类型
print(type(result))
# 编码
print(result.encoding)
# 状态吗
print(result.status_code)
# cookies
# print(result.cookies)
# 网页内容
# print(result.text)
# 以字节的形式拿到网页
# print(result.content.decode('gbk'))

## get请求  参数会显示在url地址当中，私人信息直接泄露
# 测试get请求的网站
par = {'name':'joe','pwd':'123'}#,"User-Agent":}
result = requests.get('http://httpbin.org/get',params= par)
# print(result.text)
# 一般使用直接将参数放到get后面去

# get请求伪装成浏览器
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
# 'referer': ''  表示这个请求从哪里来的，可能会验证这个的
# 'header':''
# 'cookie':''
result = requests.get('http://httpbin.org/get',headers = headers)
# print(result.text)

# 请求知乎网站
result = requests.get('http://www.zhihu.com',headers = headers)
print(result.status_code)
# print(result.text)

# 解析json数据
result = requests.get('http://github.com/timeline.json')
# 将json解析成dict
# print(result.json())
print(type(result.json()))
# 用模块解析数据
# json.loads(result.text)
# json.dumps()

# get请求获取原始相应内容
# 1.下载音乐
url = 'http://dl.stream.qqmusic.qq.com/C4000008SUNb0SselN.m4a?vkey=07F39A7DBA4EFB1F9B3726D23C21F42A56D3D81D7B586B951C5C9080DAC545D5BF12F2D1133C36F1AF3CC4B793A5408BA2B909B33442F8D8&guid=2177108040&uin=0&fromtag=66'
result = requests.get(url,stream = True).raw.read()
# with open('aaa.mp3','wb') as file:
#     file.write(result)

# 2.下载图片
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1531558507&di=24a26dc5b119cee7947d5f111c351b5d&imgtype=jpg&er=1&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F01690955496f930000019ae92f3a4e.jpg%402o.jpg'
result = requests.get(url,stream = True).raw.read()
# with open('aaa.jpg','wb') as file:
#     file.write(result)

# 发送cookies
headers = {'cookie':'id007'} #放在这儿提交
result = requests.get('http://httpbin.org/cookies',headers = headers)
# print(result.text)

'''
{"args":{},
 "headers":
     {"Accept":"*/*","Accept-Encoding":"gzip, deflate",
      "Connection":"close",
      "Host":"httpbin.org",
      "User-Agent":"python-requests/2.19.1"},
      "origin":"218.98.26.43",
      "url":"http://httpbin.org/get"}

"User-Agent"身份信息
'''
# post请求。url中参数是隐藏的
data = {'user':'joe','id':'007'}
result = requests.post('http://httpbin.org/post',data = data)
print('post：',result.text)


# session，开启了之后就相当于在同一个浏览器里面操作
# session设置cookie
'''
res = requests.get('.../setcookie')
print(res.text)
# 看设置了什么
res = requests.get('.../cookie')
print(res.text) #这个会没有显示的，因为是两个requests独立的

# 这样做,就是在同一个会话里完成的，就可以完成设置
s = requests.session()
res = s.get('.../setcookie')
print(res.text)
res = s.get('.../cookie')
print(res.text)
'''

'''
# session模拟登陆
import json
url = 'http://123.207.11.209:8080/index.php/Home/Index/'
s = requests.session()
res = s.post()
'''


# 代理请求
proxies = {'http':'111.155.116.210:8123'}
headers = {"User-Agent":
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

url = 'http://httpbin.org/get'
res = requests.get(url,proxies = proxies)
print(res.text)
# 210.13.127.204

# SSL验证
# verify = False
url = 'http://www.12306.com'
res = requests.get(url,verify = False)
# print(res.text)