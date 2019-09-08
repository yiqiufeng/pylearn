"""
coding:utf-8
文件名称：004_list.py
功能：

"""

# 使用list函数定义空列表
l= list()
#使用中括号定义空列表
l=[]
#使用中括号定义带初始值的列表
l =[1,2,3]
#使用list函数把可迭代对象转换为列表
l=list(range(1,10))
print(l)

help(list.index)

help(list.count)

help(list.append)
help(list.insert)
help(list.extend)

new_l.insert(i,e)
new_l.insert(1,2)
new_l.insert(0,'e')
new_l.insert(100,'d')

"""

def index(lst,value,start=0,stop =-1):
    #定义一个起始位置，这个起始位置就是我们list里的start
    i = start
    #通过循环来迭代list对象，同时这里用到一个分片的概念；
    for x in lst(start:stop)
        #value是我们要查找的值，当value存在，就返回当前的i
        if x==value:
            return i
        i += 1
    #当for循环结束，还没有遇到错误的时候，就抛出一个异常；
    raise ValueError()
    
"""
def count(lst,value):
    #这个c就是计数器了，用来统计我们要找的value在list里有多少个；
    c = 0
    for x in lst:
        #循环列表的每个元素，当元素和value的值相等的时候，计数器c就加1
        if  x == value:
            c += 1
    return c




