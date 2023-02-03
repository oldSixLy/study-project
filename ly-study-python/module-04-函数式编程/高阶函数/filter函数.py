# filter()
# 把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

# 删除列表中的偶数
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
    return s and s.strip() # strip()用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))