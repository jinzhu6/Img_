#coding=utf-8

import time
import numpy as np

## 数组拉伸与合并
arr1 = np.random.randint(1,9,(2,2))
# 使用tile进行拉伸
arr2 = np.tile(arr1,2)
print(arr1)
print(arr2)
# 横向和纵向拉伸
arr3 = np.tile(arr1,(3,2))
print(arr3)
# 合并stack
a = [1,2,3,4]
b = [10,20,30,40]
# 默认0轴合并
print(np.stack((a,),axis=0))
print(np.stack((a,),axis=1))

print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))

c = [[1,2,3,4],[5,6,7,8]]
d = [[10,20,30,40],[50,60,70,80]]
print('一个lis',np.stack((c,),axis=0))
print('一个lis',np.stack((c,),axis=1))
print('一个lis',np.stack((c,),axis=2))

print('两个lis',np.stack((c,d),axis=0))
print('两个lis',np.stack((c,d),axis=1))
print('两个lis',np.stack((c,d),axis=2))

# vstack垂直，hstack水平
print('纵向',np.vstack((c,)))
print('纵向',np.vstack((c,d)))

print('横向',np.hstack((c,)))
print('横向',np.hstack((c,d)))

import time
# print(time.mktime(time.time()))
three = time.time() - 3* 24 * 60 * 60
time_tup = time.localtime(three)
print(time.strftime('%Y-%m-%d %H:%M:%S',time_tup))