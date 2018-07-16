#coding=utf-8

import pandas as pd
import numpy as np

# Series创建,类似一维数组的对象
ser01 = pd.Series([1,2,3,4])
print(ser01)
ser02 = pd.Series(np.random.randint(1,9,5))
print(ser02)
dict1 = {'a':1,'b':1,'c':3}
ser03 = pd.Series(dict1)
print(ser03)
print(ser03.index)
print(ser03.values)
print(ser03.dtype)

# 修改设置index
ser02.index = list('abcde')
print(ser02)
# 创建时指定index
ser04 = pd.Series(np.random.randint(1,9,4),index=['a','b','c','d'])
print(ser04)

# 常见属性
ser04.name = '帅哥'
print(ser04)
ser04.index.name = '编号'
print(ser04)
print(ser04.axes)
print(ser04.ndim)
print(ser04.empty)
print(ser04.size)
print(ser04.head(3)) #前几个
print(ser04.tail(3)) #后几个

# 值获取
ser05 = pd.Series(np.random.randint(1,9,5),index=['a','b','b','c','d'])
# 索引获取
print(ser05['a'])
print(ser05[['a','c']])
# \切片
print(ser05['a':'c'])
print(ser05['b':'d'])
# 通过数字下标获取,和列表类似，但是相同索引是出错的，要注意
print(ser04[3])
# series的运算与标量
ser01 = pd.Series(np.random.randint(1,9,5))
print(ser01)
print(ser01+2)
# series与series运算
ser02 = pd.Series(np.random.randint(1,9,5))
print(ser01+ser02)
# 直接使用numpy函数
print(np.log(ser02))
# 条件
print(ser02[ser02>5])
# series自动对齐,对于无法通过下标对应的数字被重新赋值为Nan
ser01 = pd.Series(np.random.randint(1,9,5),index=list('abcde'))
ser02 = pd.Series(np.random.randint(1,9,5),index=list('bcdef'))
print(ser01 + ser02)
print(np.isnan(ser01 + ser02))
print((ser01 + ser02)[np.isnan(ser01 + ser02)])
print((ser01 + ser02)[~np.isnan(ser01 + ser02)])
# 缺失值检测isnull
ser01 = ser01 + ser02
print(ser01.isnull())
print(~ser01.isnull())
print(ser01[ser01.isnull()])
print(ser01[ser01.notnull()])

## DataFrame
# 通过列表创建
lis1 = [[1,2,3,4],[5,6,7,8]]
df01 = pd.DataFrame(lis1)
print(df01)
print(df01.index)
print(df01.columns)
print(df01.values)
# s通过series创建
ser01 = pd.Series([1,2,3,4])
df02 = pd.DataFrame(ser01)
print(df02)
ser02 = pd.Series([5,6,7,8])
df02 = pd.DataFrame([ser01,ser02])
print(df02)
# 通过数组创建
arr = np.random.randint(1,9,(3,3))
df03 = pd.DataFrame(arr)
print(df03)
# 通过字典创建
dict1 = {
    'name':['joe','anna','yili'],
    'age':[18,19,20],
    'class':1 #整列数据会被标量填充
}
df03 = pd.DataFrame(dict1)
print(df03)
# 重置索引
df03.index = list('abc')
print(df03)
df04 = df03.reset_index(drop=True)
print(df04)

df03.columns = list('ABC')
print(df03)
# 列值获取
# 查
df03.reset_index()
print(df03)
print(df03['A'])
print(df03[['A','B']])
# 增
df03['address']=['usa','cha','uk']
print(df03)
# 删,会返回被删除的内容
print(df03.pop('address'))
# del删除
# del(df03['address'])
print(df03)
# 改
df03['B']= [3,4,5]
print(df03)
# 行操作
# 查
print(df03.ix[0])
print(df03.ix[[0,2]])
# 选择某行某列
print(df03.ix[0,'A'])
print(df03.ix[[0,2],['A','B']])
# 切片
print(df03.ix[1:,'A':'B'])
# 使用iloc数字索引
# print(df03.iloc[0])
# 增加
df03.ix['d'] = [18,6,'ronado']
print(df03)
# 删除,返回新的df，原来的不改变
print(df03.drop('d'))
# 改
df03.ix['c'] = [20,3,'luban']
print(df03)

## 数据文件读取
# read_xxx之类
# 读取scv
data = pd.read_csv('data1.csv')
print(data)
data.to_csv('data2.csv')
# 读取文本
data2 = pd.read_csv('data1.txt',sep='	')
print(data2)
data2.to_csv('data2.txt',sep = ':')
data2.to_csv('data3.txt',sep = ':',header= None)
print('111;.',pd.read_csv('data1.txt',sep='	',header= None)) #不带头
# 读取excel,这里要安装xlrd库文件才行
# data3 = pd.read_csv('data1.xlsx',)
# print(data3)
print(pd.__version__)
# 缺失值处理
df01 = pd.DataFrame(np.random.randint(1,9,(4,4)),index=list('ABCD'),columns=list('abcd'))
print(df01)
df01.ix['B','b'] = np.NaN
df01.ix['C','c'] = np.NaN
print(df01)
print(df01['b'].isnull())
# dropna.默认删除行，返回新的df
print(df01.dropna())
# 设置阈值，删除整行都nan的
df01.dropna(how= 'all')
df01.ix['E'] = np.NaN
print(df01)
# fillna处理
print(df01.fillna(0))
print(df01.fillna(method='ffill')) #根据前一个值进行替换
print(df01.fillna(method='bfill')) #根据后一个值进行替换
print(df01.fillna({'b':100,'c':300})) #根据列进行替换
print(df01.replace({np.NaN:'hhhh'})) #根据值进行替换

## 数学统计函数
# count
print(df01.count())
print(df01.count(axis= 1))
ser01 = pd.Series(np.random.randint(1,5,6),index = list('abcdef'))
print(ser01)
print(ser01.count())
# describe
print(df01.describe())
# min
print(df01.min(axis = 1))
# idxmin/idxmax 最小/大值的行索引
print(df01.idxmin())
# sum
print(df01.sum())
print(df01.sum(axis = 1))
# mad
print(df01.mad())
print(df01.mad(axis = 1))
# cumsum,样本累计和
print(df01.cumsum())
# pct_change,后续和前面变化差
print(df01.pct_change())
## 相关系数he协方差
df01 = pd.DataFrame({
    'kill':[5,6,7,8],
    'duanwei':[1,2,3,4]
})
print(df01)
print(df01['kill'].cov(df01['duanwei']))
print(df01['kill'].corr(df01['duanwei']))
# 唯一值。值计数，成员资格
ser01 = pd.Series(np.random.randint(1,5,6),index = list('adcdef'))
print(ser01.unique())
print(ser01.value_counts())# 查看改值出现的次数
print(ser01.isin([1,3]))
print(ser01.index.isin(['a','c']))

df01 = pd.DataFrame(np.random.randint(1,6,(5,5)),index=list('ABCDE'),columns=list('abcde'))
print(df01)
print(df01['a'].unique())#只能某一列或行
print(df01['a'].value_counts().head(3)) #从高到低将重复的排列

## 层次索引
ser01 = pd.Series([30,33,35,18,20,30],index = [
    [2017,2017,2017,2018,2018,2018],
    ['mseei','cr7','nermae','mseei','cr7','nermae']
])
print(ser01)
print(ser01[2017])
print(ser01[2017]['mseei'])
print(ser01[2018]['cr7'])
print(ser01[:,'nermae'])
# 转换成dataframe
df00 = ser01.unstack(level = 1)
print(df00)
print(df00.stack())

# dataaframe
df01 = pd.DataFrame({
    'year':[2017,2017,2017,2018,2018,2018],
    'goal':[30,33,35,18,20,30],
    'name':['mseei','cr7','nermae','mseei','cr7','nermae']
})
df02 = df01.set_index(['year','name'])
print(df02)
print(df02.loc[2017,'mseei'])
print(df02.loc[2017,'mseei']['goal'])
# 变来变去
print(df02.unstack())
print(df02.unstack().stack())
print(df02.sum(level = 'year'))
print(df02.sum(level = 'name'))

## 排序
# sort_index
ser01 = pd.Series([1,2,3,4,5],index = list('bcdae'))
print(ser01.sort_index(0))
print(ser01.sort_index(ascending= False)) #升讲

df01 = pd.DataFrame(np.random.randint(1,9,(4,4)),index= list('BCDA'),columns=list('adcb'))
print(df01.sort_index(axis=0))
print(df01.sort_index(axis=1))

# sort_values
ser01 = pd.Series([3,4,2,5,1])
print(ser01.sort_values())
print(df01.sort_values(by = 'a')) #按照a排序
print(df01.sort_values(by = ['a','c'])) #先按照a，后c排序

# rank,排名，相等的会分别占用第二名和第三名，排名为2+3的一半
ser01 = pd.Series([4,5,2,2,1])
print(ser01.rank())
print(ser01.rank(method = 'min')) #按小的算
print(ser01.rank(method = 'max')) #按da的算
print(ser01.rank(method = 'first')) #按先后出现顺序

## 时间序列
df01 = pd.date_range(start = '20180701',end = '20180708')
print(df01)
df02 = pd.date_range(start = '20180701',end = '20180708', freq = '2d') #按2天跑一次
print(df02)
df01 = pd.date_range(start = '20180701',periods = 10, freq = '10min') #10条数据，10分间隔
print(df01)
df01 = pd.date_range(start = '20180701',periods = 10, freq = 'm') #10条数据，按月末走
print(df01)

# 表合并
df01 = pd.DataFrame({
    'data1':[1,2,3,4,5],
    'key1':list('abcde')
})
df02 = pd.DataFrame({
    'data1':[6,7,8,9,10],
    'key1':list('abcde')
})
# merge
df03 = pd.merge(df01,df02,on = 'key1')
print(df03)
df03 = pd.merge(df01,df02,on = 'key1',how = 'inner') #添加链接方式
print(df03)
df02 = pd.DataFrame({
    'data1':[6,7,8,9,10],
    'key1':list('abgde')
})
df03 = pd.merge(df01,df02,on = 'key1',how = 'inner') #添加链接方式,交集保留
print(df03)
df03 = pd.merge(df01,df02,on = 'key1',how = 'outer') #添加链接方式,丙级
print(df03)
df03 = pd.merge(df01,df02,on = 'key1',how = 'left') #添加链接方式,左边，没有nan补齐
print(df03)
df02 = pd.DataFrame({
    'data1':[6,7,8,9,10],
    'key2':list('abgde')
})
df03 = pd.merge(df01,df02,left_on = 'key1',right_on = 'key2',how = 'inner') #添加链接方式,左边
print(df03)
# concat 沿着一条轴合并
df01 = pd.DataFrame({
    'data1':[1,2,3,4,5],
    'key1':list('abcde')
})
df02 = pd.DataFrame({
    'data2':[6,7,8,9,10],
    'key1':list('abcde')
})
df03 = pd.concat([df01,df02],join = 'outer') #纵向
print(df03)
df02 = pd.DataFrame({
    'data2':[6,7,8,9],
    'key2':list('abcd')
})
df03 = pd.concat([df01,df02],join = 'outer',axis = 1) #横向
print(df03)

# 分组
df01 = pd.DataFrame({
    'data1':[1,2,3,4,5],
    'data2':[10,20,30,40,50],
    'key1':list('abaab'),
    'sex':list('mwmww')
})
print(df01)
df02 = df01.groupby('key1')
print(list(df02))
print(df02.mean())
print(df02['data1'].mean())
print(df01.groupby(['key1','sex'])['data2'].max())

# 聚合apply
print(df01.groupby(['key1','sex'])['data2'].apply(lambda x:x.max()))
print(df01.groupby('sex')['data2'].apply(lambda x:x.max()))
df01 = pd.DataFrame(np.random.randint(1,9,(4,4)),index = list('ABCD'),columns = list('abcd'))
print(df01)
print(df01.apply(lambda x:x+10)) #默认按列操作，x就是一列一列的数据

#pandas之数据透视
df01 = pd.DataFrame({
    'kill':[1,2,3,4,5],
    'address':['pikaduo','shengmading','pikaduo','shengmading','pikaduo'],
    'help':[3,4,2,5,2],
    'sex':list('mwmmw')
})
print(df01)

# 通过index 进行分组查看values中的字段的aggfunc 的值,和groupby()
df02 = df01.pivot_table(values = ['kill','help'],index = ['address'],aggfunc = np.mean)
print(df02)
print(df01.groupby('address')['kill','help'].mean())
df02 = df01.pivot_table(values = ['kill','help'],index = ['address'],aggfunc = [np.mean, np.min, np.max])
print(df02)
df02 = df01.pivot_table(values = ['kill','help'],index = ['address'],columns = ['sex'], aggfunc = np.mean)
print(df02)

data1 = pd.read_csv('ca_list_copy.csv')
print(data1)