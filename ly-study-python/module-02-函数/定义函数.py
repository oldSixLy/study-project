# 定义函数时，需要确定函数名和参数个数；

# 如果有必要，可以先对参数的数据类型做检查；

# 函数体内部可以用return随时返回函数结果；

# 函数执行完毕也没有return语句时，自动return None。

# 函数可以同时返回多个值，但其实就是一个tuple。

# 定义函数
def return_many_results():
    value1 = 'Hello'
    value2 = 'World!'
    return value1, value2

# 实际返回值为一个元组
print(return_many_results())

# 多个变量可以同时接收一个tuple，按位置赋给对应的值
x1, x2 = return_many_results()
print(x1)
print(x2)


# 返回一元二次方程的两个解。
from my_private.util import quadratic

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
