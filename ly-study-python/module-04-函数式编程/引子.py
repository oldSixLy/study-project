# 变量可以指向函数

# 以Python内置的求绝对值的函数abs()为例:
#   abs()是函数调用，abs是函数本身
# 函数本身也可以赋值给变量，即：变量可以指向函数。
f = abs
print(f)
# 直接调用abs()函数和调用变量f()完全相同。

# 函数名也是变量

# abs = 10
# print(abs)
# 注：由于abs函数实际上是定义在import builtins模块中的，
# 所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。

# 传入函数

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为 *高阶函数*。
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))


# 编写高阶函数，就是让函数的参数能够接收别的函数。
