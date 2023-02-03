# 由于函数也是一个对象，
# 而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2015-3-25')

f = now
f()

# 现在，假设我们要增强now()函数的功能，比如，
# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# 本质上，decorator就是一个返回函数的高阶函数。
# 所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，
# 并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def studyNow(time):
    print('2023-1-30  ',time)

from datetime import datetime
currentDateAndTime = datetime.now().strftime("%H:%M:%S")

studyNow(currentDateAndTime)
# 把@log放到studyNow()函数的定义处，相当于执行了语句：studyNow = log(studyNow)
# ！！！！！！！！！！！！！！！！！！！！！！！！！
# 也就是说执行studyNow(currentDateAndTime)实际上执行的是在log()函数中返回的wrapper()函数。
# ！！！！！！！！！！！！！！！！！！！！！！！！！

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
# 写出来会更复杂。比如，要自定义log的文本：

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 这个3层嵌套的decorator用法如下：

@log('execute')
def now():
    print('2015-3-25')

now()
# now = log('execute')(now)

# ---------------------------------------------------------
print(now.__name__) # 由此可知，返回wrapper()的函数名字
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖函数签名的代码执行就会出错。

# 不需要编写wrapper.__name__ = func.__name__这样的代码，
# Python内置的functools.wraps就是干这个事的，
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()
print(now.__name__)


# ------------------------练习---------------------------------

import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        begin = time.time()
        fnr = fn(*args, **kw)
        print('%s executed in %.4f ms' % (fn.__name__, time.time() - begin))
        return fnr
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')