# 小明身高1.75，体重80.5kg。
# 请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = float(input('请输入身高(m)：'))
weight = float(input('请输入体重（kg）：'))

BMI = weight / (height**2)
if BMI < 18.5 :
    print('过轻')
elif 18.5 <= BMI < 25:
    print('正常')
elif 25 <= BMI < 28:
    print('过重')
elif 28 <= BMI < 32:
    print('肥胖')
else :
    print('严重肥胖')