# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
# 并用字符串格式化显示出'xx.x%'，只保留小数点后1位

last_score = 72
current_score = 85
promote_percentage = (current_score - last_score) / last_score * 100
print(f'{promote_percentage:.1f}%')
