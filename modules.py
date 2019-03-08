import requests as req
from enum import IntEnum
from html.parser import HTMLParser
import abc
import sys
from requests.auth import HTTPBasicAuth
import json
import os
import execjs

# 爬取erp页面
path = 'save.html'

url = 'http://source.com'
# url = 'http://www.baidu.com'

auth = {'username': '',
        'password': ''}

class c1:
    hello = '12'
    lk = 12

class method_type:
    POST = 'post'
    GET = 'get'

class c2(c1, method_type):
    f1 = '123'
    f2 = '098'
    GET = 21

    @staticmethod
    def m1():
        print('静态方法: ' + c2.f1)

    @classmethod
    def m2(self):
        print('类方法：'+self)
        print(c2.f2)

    @abc.abstractmethod
    def m3(self):
        pass


z = lambda x, y: x * y

print("lambda 表达式 " + str(z(2, 6)))

class status_code(IntEnum):
    OK = 200  # 成功
    REDIRECT = 302  # 重定向
    METHOD_NOT_SUPPORT = 405  # 方法不支持


ins = c2()
ins.m1()

print(c2.GET)

print(ins.m1())

# 发起请求
def res(u, method=method_type.POST):
    if method == method_type.GET:
        response = req.get(u, allow_redirects=False)
    else:
        response = req.post(u, allow_redirects=False)
    print("返回响应码："+str(response.status_code))
    # 返回码
    code = response.status_code

    # 如果是重定向，递归调用
    if code == status_code.REDIRECT:
        # 获取重定向地址
        location = response.headers.get('Location')
        print("重定向地址：" + location)
        res(location)
    # 如果成功
    elif code == status_code.OK:
        # 写入文件，分析js source，调用js执行引擎
        with open(path, 'w+') as fd:
            fd.write(response.text)
    # 如果方法不支持，换成get
    elif code == status_code.METHOD_NOT_SUPPORT:
        res(u, method_type.GET)

    else:
        print("返回异常响应码:" + str(response.status_code))
        print("返回信息: " + response.text)

# 解析html文件
class HtmlPa(HTMLParser):

    def __init__(self, path):
        self.__path = path
        self._na = None

    def _s_(self):
        pass

    def sa(self):
        pass

sl = HtmlPa('windows')
print(sl._na)
sl._na = '121'
print(sl._HtmlPa__path)
print(sl._na)

res(url)

t = {'str': '1', 'bool': '2'}

s = tuple(t)

print(isinstance(t, tuple))

print(type(t))

print('-------------')
print(bool('ss'))



'''
函数定义语法
def 函数名(参数):

    return

参数有以下几种类型定义：
必须参数 p：
def m1(name):
    print('name: '+name)
    
默认参数 p=default：默认参数的默认值一般设置为不可变对象，例如tuple，str
def m2(name, age=6):
    print('name: ' + name + 'age: ' + age)
    
可变参数 *p：
def m3(name, age=6, *address)
    print()
    
关键字参数 **p：
def m4(name, age=6, *address, **city)
    
命名关键字参数：指定关键字参数的名称
def m5(name, age=1, *, d, n, **keys)
def m6(name, age=2, *p, d, n, **keys)

参数定义顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

!!参数类型的判定
type()
isinstance()

python的内置对象
内置对象定义在builtins.py资源文件中，以下是一些常用内置对象
tuple
set
list
str
enumerate
int
float
bool

python常用内置函数


python访问数据的一些特性。切片，迭代， 列表生成式， 生成器，迭代器

切片：


'''





'''

python 类定义

语法：
class 类名(父类1, 父类2)：
    类属性
    def 方法()

'''
