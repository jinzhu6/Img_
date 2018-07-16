# coding=utf-8
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

url = 'http://www.baidu.com'
response = requests.get(url).content.decode('utf-8')
# print(response)

# 使用bs4 解析请求到的html文档
soup = BeautifulSoup(response, 'lxml')# 或者'html.parser')
#             他们的解析速度快，容错率高
print(type(soup))

# 格式美化，方便找
# print(soup.prettify())

# 打开本地的html文件，url直接是文件名称就行
result = BeautifulSoup(open('web.html',encoding= 'utf-8'),'html.parser')
# print(result)

# BeautifulSoup节点遍历
# 四大对象
# Tag
# div标签就相当一个盒子
# content是主题内容部分
print(type(result.html.body)) #默认会找整个文档中第一个名字叫这个的Tag

# NavigabString  标签中的文本
# 如果用string,必须保证里面没有子标签
print(result.html.body.span)#.a.string)
# <span>logo  <a href="http://www.taobao.com">taobao</a></span>
print(result.html.body.span.a.string)
# strings , 获取多个文本,有子标签情况下也可使用
str_h = result.html.body.div.span.strings
for i in str_h:
    print(i)


# 如何让遍历文档树
# 1.直接子节点,可以获取该节点下的所有子节点，包括换行符
list1 = result.html.body.div.contents
print(list1) #列表
# 获取淘宝
print(list1[1])
# 不好，空格没办法规避
print(result.html.body.div.children)
print('-'*20)
for i in result.html.body.div.children:
    print(i)

# 2.递归所有子孙节点
print(result.html.body.div.descendants)
for i in result.html.body.div.descendants:
    print(i)

print('-'*40)

# 3.重点
# 获取该标签下的所有文本，和string还是有很大区别的
print(result.html.body.div.span.text)

# 4.获取当前节点的父节点
print(result.html.body.div.span.a)
print(result.html.body.div.span.a.parent)
print(result.html.body.div.span.a.parent.parent)
print(result.html.body.div.span.a.parents)
for i in result.html.body.div.span.a.parents:
    print(i)

# 5.获取兄弟节点,换行符也算是节点的，这里有个平级的换行
print(result.html.body.div.next_sibling.next_sibling)

# 6.

# 1.发送请求，获取源码
# 2.解析源码
# 3.提取相关标签以及文本内容
