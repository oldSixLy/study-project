# 列表（可变）
list = ['001','002', '003']
# 元组（不可变，有序集合）如果只有一个元素要加，
tuple_right = (1,)
tuple_error = (1)

print(list)
print(tuple_right)
print(tuple_error)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印‘Lisa’
print(L[-1][-1])

# list方法
classmates = ['Michael', 'Bob', 'Tracy']

print(len(classmates))

# 追加元素到末尾
classmates.append('Adam')
classmates.append('test1')
print(classmates)

# 把元素插入到指定的位置
classmates.insert(2, 'Jack')
print(classmates)

# 删除list末尾的元素
classmates.pop()
print(classmates)

# 删除指定位置的元素
classmates.pop(2)
print(classmates)
