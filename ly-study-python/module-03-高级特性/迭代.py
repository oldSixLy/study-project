# 判断迭代对象
# collections.abc模块的Iterable类型判断
from collections.abc import Iterable, Iterator

# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
flag1 = isinstance('abc', Iterable) # str是否可迭代
flag2 = isinstance([], Iterable)
print(flag1)
print(flag2)

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
print(isinstance([], Iterator))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
# 为什么list、dict、str等数据类型不是Iterator？

# 这是因为Python的Iterator对象表示的是一个数据流，
# Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，
# 但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。
# 而使用list是永远不可能存储全体自然数的。


# 练习：
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if (len(L) == 0):
        return (None, None)

    # max = L[0]
    # min = L[0]
    max = 0
    min = 0
    # Python内置的enumerate函数可以把一个list变成索引-元素对
    for i,v in enumerate(L):
        if (i == 0):
            max = v
            min = v
        elif (v > max):
            max = v
        elif (v < min):
            min = v

    return min, max

# 测试
print(len([]) == 0)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')