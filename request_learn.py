"""
coding:utf-8
文件名称：request_learn.py
功能：get演示
：return

"""
def get_demo():

    import  requests
    playload = {'name':'jim', 'age':18}
    res=requests.get('http://httpbin.org/get',params =playload)
    print(res.text)
    print(res.status_code)
    print(res.headers)
    pass

if __name__ == '__main__':
    get_demo()
pass