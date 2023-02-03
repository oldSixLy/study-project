# 函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print('调用lazy_sum()返回求和函数:\n',f)
print('--------------------------------')
print('调用f返回求和结果:\n',f())

# 我们在函数lazy_sum中又定义了函数sum，并且，
# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2) # f1()和f2()的调用结果互不影响。

# 返回的函数并没有立刻执行，而是直到调用了f()才执行。
# 注意：
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
# 原因就在于返回的函数引用了变量i，
# 但它并非立刻执行。等到3个函数都返回时，
# 它们所引用的变量i已经变成了3，因此最终结果为9。

# 返回闭包时牢记一点：
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

# -----------------------------------------------------
# 使用闭包，就是内层函数引用了外层函数的局部变量。
# 如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常：
def inc():
    x = 0
    def fn():
        # 仅读取x的值:
        return x + 1
    return fn

f = inc()
print(f()) # 1
print(f()) # 1
print('-------------')
# 但是，如果对外层变量赋值，
# 由于Python解释器会把x当作函数fn()的局部变量，它会报错：
def inc():
    x = 0
    def fn():
        nonlocal x # 声明该变量不是当前函数的局部变量。
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2
# 原因是x作为局部变量并没有初始化，直接计算x+1是不行的。
# 但我们其实是想引用inc()函数内部的x，
# 所以需要在fn()函数内部加一个nonlocal x的声明。
# 加上这个声明后，解释器把fn()的x看作外层函数的局部变量，它已经被初始化了，可以正确计算x+1。

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

# -*- coding: utf-8 -*-
def createCounter():
    x=0
    def counter():
        nonlocal x
        x += 1
        return x
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')