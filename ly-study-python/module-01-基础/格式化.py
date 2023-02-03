# %运算符就是用来格式化字符串的
a = 'Hello, %s' % 'world'
b = 'Hi, %s, you have $%.2f.' % ('Michael', 1000000)


# format()
c = 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)


# f-string
r = 2.5
s = 3.14 * r ** 2
d = f'The area of a circle with radius {r} is {s:.2f}'

for i in [a, b, c, d]:
    print(i)