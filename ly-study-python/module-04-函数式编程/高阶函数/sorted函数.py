# 普通排序
v1 = sorted([36, 5, -12, 9, -21])

# 自定义排序
v2 = sorted([36, 5, -12, 9, -21], key=abs)

print(v1,v2)

# 默认情况下，对字符串排序，是按照ASCII的大小比较的

# 由于Z小于a
# 忽略大小写的排序
v3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(v3)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按名字排序
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

# 按分数排序
def by_score(t):
    return -t[1]

L2 = sorted(L, key=by_score)
print(L2)

L3 = sorted(L, key=lambda a:a[1], reverse=True)
print(L3)