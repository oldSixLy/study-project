# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)

# 打印出generator的每一个元素,next()函数
# generator保存的是算法，每次调用next(g)，
# 就计算出g的下一个元素的值，直到计算到最后一个元素，
# 没有更多的元素时，抛出StopIteration的错误。
# 因为generator也是可迭代对象,可搭配for循环
g = (x * x for x in range(3))
for n in g:
    print(n)

def test(*param):
    for n in param:
        print(n)

test(*(x * x for x in range(3)))

# generator生成器函数
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n+1] for n in range(len(L)-1)] + [1]

for i in triangles():
    print(i)
    n = n + 1
    if n>5:
        break
    
