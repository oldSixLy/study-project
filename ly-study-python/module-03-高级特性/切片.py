from operator import index


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 第一个是0
# 倒数第一个元素的索引是-1

# 从索引1开始取，直到索引3为止，但不包括索引3。
value1 = L[1:3]

# 从索引0开始
value2 = L[:3]

# 从倒数第二个开始
value3 = L[-2:]

# 从倒数第二个开始，截至并不取第一个
value4 = L[-2:-1]

# 0-99的数列
L = list(range(1,100))

# 取11到20(1开头)
value5 = L[10:20]

# 所有数，每5个取一个
value6 = L[::5]

# 前10个数，每两个取一个
value7 = L[:10:2]

# 原样复制一个list
value8 = L[:]

# --------------tuple-----------------

# tuple的切片操作，操作结果仍是tuple
value9 = (0, 1, 2, 3, 4, 5)[:3]

# --------------字符串-----------------

# 字符串的切片操作，操作结果仍是字符串
value10 = 'ABCDEFG'[:3]

# --------------练习-----------------

# 利用切片操作，实现一个trim()函数

def my_trim(s) :
    if (len(s) == 0):
        return s
    else:
        while s[0] == ' ':
            s = s[1:]
        while s[-1] == ' ':
            s = s[:-2]
        return s

# 递归
def my_trim2(s):    
    if(len(s) == 0):        
        return s    
    elif(s[0] == ' '):       
        return my_trim2(s[1:])    
    elif(s[-1] == ' '):        
        return my_trim2(s[:-1])    
    else:
        return s





# -----------------------------------
# Test

# list
print(value1)
print(value2)
print(value3)
print(value4)
print(value5)
print(value6)
print(value7)
print(value8)

# tuple
print(value9)

# 字符串
print(value10)

print('-' + my_trim('      abc   def    ') + '-')

print('-' + my_trim2('      abc   def    ') + '-')
print('-' + my_trim('') + '-')
print('-' + my_trim2('') + '-')