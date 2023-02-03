# 生成[1x1, 2x2, 3x3, ..., 10x10]

# 1.循环方法（笨拙）
L1 = []
for x in range(1,11):
    L1.append(x * x)
print(L1)
# 2.列表生成式
L2 = [x * x for x in range(1, 11)] # 要生成的元素x * x放到前面，后面跟for循环
print(L2)

# 仅偶数的平方，后面跟if判断
L3 = [x * x for x in range(1, 11) if(x % 2 == 0)]
print(L3)
# 在一个列表生成式中，for前面的if ... else是表达式
# 而for后面的if是过滤条件，不能带else
[x if x % 2 == 0 else -x for x in range(1, 11)]


# 使用两层循环，可以生成全排列
L4 = [m + n for m in 'abc' for n in '123']
print(L4)

# 列出当前目录下的所有文件和目录名
import os
print([file_name for file_name in os.listdir('C:\\Users\ZZ0EGL672\Desktop\GDP_テーブル定義書_Conformed_v1')])

# 练习
array = ['Hello', 'World', 18, 'Apple', None]
filter_array = [s.lower() for s in array if(isinstance(s,str))]

# 测试:
print(filter_array)
if filter_array == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')