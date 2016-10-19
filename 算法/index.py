#!/usr/bin/python3
# coding:utf-8

'''
Created on:
@author:
Email:
Version:
Description:一些算法的描述
Help:http://www.cnblogs.com/wupeiqi/articles/5480868.html
'''

'''
递归
程序本身自己调用自己称为递归，类似于俄罗斯套娃
'''
def func(arg1, arg2):
    # count += 1
    if arg1 == 0:
        # count = 0
        print(arg1, arg2)

    arg3 = arg1 + arg2
    print(arg3)
    if count < 100:
        func(arg2, arg3)


    else:
        print('progress is over!!!')

if __name__ == "__main__":
    count = 0
    func(0, 1)

'''
=======================
google发现是因为"f"作为一个变量在两个createFile函数都调用了，
在第2个createFile函数时出错，把f定义成全局变量
=======================
'''

'''
冒泡排序
利用相邻元素比较并进行位置的互换。。。
'''

'''
选择排序（先要创建一个特殊的变量）
1。选择第一个值的索引赋值给特殊变量，然后循环其他索引并进行值的比较，如果特殊变量对应的值 > 循环的值，那么将当前值的索引放入变量中，继续向后比较
2。选择第二个值的索引赋值给特殊变量，...
3。...
'''

'''
插入排序（有两个特点）
1。从前向后两两比较
2。永远保证左边是有序的

其实插入排序就是维护一个有序的序列，并且有一个人在不停的抛出新的值，
然后有序的序列开始去检测新值，将其添加到有序序列中的合法位置。
'''
