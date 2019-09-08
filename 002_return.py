"""
coding:utf-8
文件名称：002_return.py
功能：

"""
def add(x,y):
    return x+y
    print('hello')
r=add(1,2)
print(r)



def  fn(x):
    for i in range(x):
        if i>3:
            return i
    else:
        print("not bigger than 3")

p=fn(10)
print(p)

def fn():
    pass
ret=fn()
print(type(ret))
