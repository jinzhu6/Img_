#coding=utf-8

import re

'''
正则表达式进行格式验证，比如登陆的用户名和密码
'''

# 正则表达式如何制定规则


# compile,制作正则表达式的函数
pattern = re.compile('\w?')
# print(pattern)
print(type(pattern))

# match，只从字符串的开头进行匹配
pattern = re.compile('\d') #规则：一个数字
strs1 = 'abc'
strs2 = '1a'
print(re.match(pattern, strs1)) #查看匹配结果，要用group
print(re.match(pattern, strs2).group())

pattern = re.compile('(\d)[a-z]+(\d)') #规则：一个数字
strs1 = '1abc2'
print(re.match(pattern, strs1).group(0)) #返回完整的匹配结果
print(re.match(pattern, strs1).group(1)) #返回第一个分组的匹配结果
print(re.match(pattern, strs1).group(2)) #返回第二个分组的匹配结果

# search
pattern = re.compile('(\d)[a-z]+(\d)') #规则：一个数字
strs1 = 'MMM1asdas2NNN3adsf4KKKK'
# 使用match，直接会报错的
print(re.match(pattern, strs1)) #返回None
# print(re.match(pattern, strs1).group(0)) #返回完整的匹配结果
# print(re.match(pattern, strs1).group(1)) #返回第一个分组的匹配结果
# print(re.match(pattern, strs1).group(2)) #返回第二个分组的匹配结果
# 使用serach, 只匹配一次，成功则停止匹配
print(re.search(pattern, strs1).group(0))
print(re.search(pattern, strs1).group(1))
print(re.search(pattern, strs1).group(2))

# findall遍历匹配
# findall遍历匹配，返回所有匹配的字符串，保存在一个列表
pattern = re.compile('\d[a-z]+\d')
strs1 = 'MMM1asdas2NNN3adsf4KKKK'
print(re.findall(pattern, strs1))

# 有分组看看
# findall 如果规则中有分组则只返回分组的匹配结果
pattern = re.compile('(\d)[a-z]+(\d)')
strs1 = 'MMM1asdas2NNN3adsf4KKKK'
print(re.findall(pattern, strs1))

# 解决方法
# finditer
pattern = re.compile('(\d)[a-z]+(\d)')
strs1 = 'MMM1asdas2NNN3adsf4KKKK'
print(re.finditer(pattern, strs1))
for i in re.finditer(pattern, strs1):
    print(i.group(0))#查看分组的匹配内容
    print(i.group(1))
    print(i.group(2))


# split()分割
# 返回切割后的列表，按照符合正则的字串
print(re.split('\d','s32df32f32'))

# sub()替换,要加引号的
print(re.sub('[a-z]','obj','s32df32f32'))

# subn()返回替换次数，和结果组成的元祖
print(re.subn('[a-z]','obj','s32df32f32'))

# 引用分组
# \1\2表示第一第二个分组匹配的内容
print(pattern.sub(r'\2 aaa \1',strs1))


## 贪婪与非贪婪
# 贪婪
strs = "<a>nnn</a><p>abc</p><script>alert('hahahaha')</script><p>efg</p><span>bbb</span>"

pattern = re.compile('<p>[a-z]+</p>')
print(pattern.findall(strs))

# 在符合规则的前提下，尽可能多的匹配
# .表示任意字符
# *表示任意长度
pattern = re.compile('<.>.*</.>')
print(pattern.findall(strs))

pattern = re.compile('<p>.*</p>')
print(pattern.findall(strs))

# 非贪婪
# ?表示尽可能少的匹配
pattern = re.compile('<.>.*?</.>')
print(pattern.findall(strs))

# 匹配中文字符串
strs = '靓仔,靓妹,你好,lucy'
pattern = re.compile('\w+')
print(pattern.findall(strs))
# 现在不想要字母，来匹配中为，有个专门匹配中文的
pattern = re.compile("[\u4e00-\u9fa5]+")
print(pattern.findall(strs))

# 练习
# 1，将一下字符串的url匹配出来
str1 = '''313354545@qq.com
    hfdskjd3@163.com
    http://www.asa.com.cn
    https://www.cba.com
    ftp://www.nnn.org
    ftps://www.jkasd.net'''
pattern = re.compile("[a-z]+://www(\.[a-z]+)(\.[a-z]+){1,2}")
for i in pattern.finditer(str1):
    print(i.group())
pattern2 = re.compile("[a-z0-9]+@[a-z0-9]+.com")
print(pattern2.findall(str1))

# 2.判断是否是全是中文
str2 = '关东是s广东省'
pattern = re.compile("^[\u4e00-\u9fa5]+$")
print(pattern.findall(str2))
if pattern.findall(str2):
    print('全是中文')
else:
    print('不全是中文')

# 3.写出一个正则表达式，过虑网页上的所有JS脚本(即把scrīpt标记及其内容都去掉)script="以下内容不显示：“
str1 = "<script    language='javascript'>alert('cc');</script><p>fdgdfgdgsdg</p><script>alert('dd');</script>"
pattern = re.compile("<script.*?</script>")
# 先试一下结果
print(pattern.findall(str1))
# 替换成空格
print(pattern.sub('',str1))


# 4.将img src的路径匹配出来
str1='''
<imgname="photo"src="../public/img/img1.png" />
<imgname='news'src='xxx.jpg' title='news' />
'''
pattern = re.compile("src=[\'\"](.*?)[\'\"]")
print(pattern.findall(str1))

# 5..将电话号码13811119999变成138****9999
phone = '13811119999'
pattern = re.compile("^(1[3578]\d)(\d{4})(\d{4})$")
for i in pattern.finditer(phone):
    print(i.group(0)) #分组的所有内容
    print(i.group(1)) #分组的第一个内容
    print(i.group(2)) #分组的第二个内容
    print(i.group(3)) #分组的第三个内容
print(pattern.sub(r'\1****\3',phone))

# 此处的\是用来转义匹配规则里面的符号的
# match从字符串开头匹配只返回第一个匹配到的
pattern = re.compile("\*[^a-c].\d")
pattern1 = re.compile("\*[^a-c]{1,5}.\d")
pattern3 = re.compile("(^a1x)")
pattern4 = re.compile("(\w+) (\w+)")
strs = 'sdfs as as,as assss'
if pattern4.match(strs):
    print(pattern4.match(strs))
    print(pattern4.match(strs).group(0))
else:
    print('None')

# search类时于match，只不过不是从开头匹配的,匹配到一个结果就会返回
pattern5 = re.compile("(\d{1})")
pattern6 = re.compile("[a-z]{2,3}")#这个2和3次是同时进行的
strs2 = '1w2wsaf34f5fw67fw8'
if pattern6.search(strs2):
    print(pattern6.search(strs2).group())
else:
    print('None')

# findall返回每一个匹配到的对象组成的列表
if pattern6.findall(strs2):
    print(pattern6.findall(strs2))
else:
    print('None')

# finditer返回每一个匹配结果的match迭代对象
pattern7 = re.compile("[a-z][a-z][a-z]")
strs3 = 'abc123efg456'
if pattern7.finditer(strs3):
    for i in pattern7.finditer(strs3):
        print(i.group(0))
        # print(i.group(1))
        # print(i.group(2))
        # print(i.group(3))
else:
    print('None')
# 分组的内容会放到group中
pattern8 = re.compile("([a-z])[a-z]([a-z])")
strs4 = 'abc123efg456'
if pattern8.finditer(strs4):
    for i in pattern8.finditer(strs4):
        print(i.group(0))
        print(i.group(1))
        print(i.group(2))
        # print(i.group(3))
else:
    print('None')
# 分割
print(re.split('\d+','as1ds2fsd3sdf4'))
print(re.split('\W+','as1,ds2,fsd3,sdf4'))

# 替换
print(re.sub('\d+','---','as1ds2fsd3sdf4'))
print(re.sub('\W+','A','as1,ds2,fsd3,sdf4'))
# 返回替换后的内容和替换了几次组成的元祖
print(re.subn('\d+','---','as1ds2fsd3sdf4'))

# 引用分组 \1第一个分组 \2第二个分组,然后按位置从新排序，更改分组的位置
pattern9 = re.compile("(\w+) (\w+)")
strs5 = 'sdfs as as,as assss'
if pattern9.finditer(strs5):
    for i in pattern9.finditer(strs5):
        print(i.group(0))
        print(i.group(1))
        print(i.group(2))
    print(pattern9.sub(r'\1--\2',strs5))
    print(pattern9.sub(r'\2--\1',strs5))
else:
    print('None')

# 贪婪匹配
strs = "<a>nnn</a><p>abc</p><script>alert('hahahaha')</script><p>efg</p><span>bbb</span>"
pattern = re.compile("<a>.*</a>")
print(pattern.findall(strs))

# 非贪婪匹配
pattern = re.compile("<p>.*</p>")
print(pattern.findall(strs))
pattern = re.compile("<p>.*?</p>")
print(pattern.findall(strs))

# 中文匹配
strs = '中文,匹配,lucy'
# 匹配字符
pattern = re.compile('\w+')
print(pattern.findall(strs))
# 现在不想要字母，来匹配中为，有个专门匹配中文的
pattern = re.compile("[\u4e00-\u9fa5]+")
print(pattern.findall(strs))

# 练习
# 1，将一下字符串的url匹配出来
str1 = '''313354545@qq.com
    hfdskjd3@163.com
    http://www.asa.com.cn
    https://www.cba.com
    ftp://www.nnn.org
    ftps://www.jkasd.net'''
pattern = re.compile("")