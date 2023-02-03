# 自定义绝对值
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


import math

# 接收3个参数，返回一元二次方程 ax²+bx+c=0 的两个解。

def quadratic(a, b, c):
    # 分母
    denominator = 2 * a
    # 分子
    numerator_add = -b + math.sqrt(b**2 - 4 * a * c)
    numerator_reduce = -b - math.sqrt(b**2 - 4 * a * c)
    return numerator_add/denominator, numerator_reduce/denominator