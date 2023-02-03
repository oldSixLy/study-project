# -*- coding: utf-8 -*-
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，
# 必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：

# ord(): 获取自负的整数表示
# chr(): 把编码转换为对应的字符
print(ord('A'))
print(chr(ord('A')))

# encode(): 编码为指定的bytes
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii')) # 超过ASCII编码范围，报错

# decode(): 解码
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))