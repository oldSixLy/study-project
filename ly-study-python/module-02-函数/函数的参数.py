# 必选参数
def power1(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# --------------------

# 默认参数

# 必选参数在前，默认参数在后
# 如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，
# 变化小的参数放后面。变化小的参数就可以作为默认参数。
def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
    return s

# 默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L
add_end()
add_end()
print(add_end())

# 我们可以用None这个不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# --------------------

# 可变参数 *
# 这些可变参数在函数调用时自动组装为一个tuple。
def calc(*numbers):
    print('可变参数：', numbers)
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2, 3))

nums = [1, 2, 3]
# 把list或tuple的元素变成可变参数
print(calc(*nums))

# --------------------

# 关键字参数 **
# 允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# 它可以扩展函数的功能。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('liu', '18', city='dalian', money='6')

message = {'city': 'dalian', 'money':'6'}

person('liu', '18', **message)

# 如果要限制关键字参数的名字，就可以用命名关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，
# args元组 kw dict
# 无论它的参数是如何定义的。

# --------------------

# 允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积

def mul(x, *numbers):
    foundation = 1
    if len(numbers) > 0:
        for num in numbers:
            foundation = foundation * num
    return x * foundation


# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')