# map():
# 一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6]) # r是一个迭代器Iterator（惰性序列），因此通过list()函数让它把整个序列都计算出来并返回一个list
print('Iterator:',r)
print('List:',list(r))

# reduce 迭代
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce

# str转换int
def fn(x, y):
    return x * 10 + y

def charToNum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(charToNum, '13579')))

# 上述代码集成
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


# -----------------------------测验1-----------------------------
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print('-----------------------------测验1-----------------------------')
print(L2)


# -----------------------------测验2-----------------------------
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，
# 可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda x, y: x * y,L)

print('-----------------------------测验2-----------------------------')
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# -----------------------------测验3-----------------------------
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    idx = s.index('.')
    L1 = s[0:idx]
    #return L1 
    L2 = s[(idx + 1):]
    f1 = reduce(lambda x, y: float(x) * 10 + float(y), L1)
    #return f1
    f2 = reduce(lambda x, y: float(x) * 10 + float(y), L2)
    return f1 + f2 / 10**len(L2) 

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
