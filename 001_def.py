"""
coding:utf-8
文件名称：001_def.py
功能：

函数
函数是对程序逻辑进行结构化的一张编程方法。
python中不允许在函数声明之前被引用或调用；
优点：进行代码复用；良好的代码复用；良好的一致性（紧内聚）
返回值：
返回0个对象None；
返回1个对象object
返回多个对象tuple

函数参数：
关键字传参；位置传参；默认值参数；单星号参数
"""
'''
def  fun_no_return():
    pass
def  fun_none_return():
    return None
def fun_obj_return():
    return 1
def fun_multi_return():
    return 2,'string'

if __name__ == '__main__':
    no_res =fun_no_return()
    a=fun_none_return()
    b=fun_obj_return()
    c=fun_multi_return()
'''

def add(x,y):
    return x+y
    print('hello')
add(1,2)