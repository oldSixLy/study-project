# Schema:       conformed_data_07.tc00104rv_kpj_maker
# Table:        tc00104rv_kpj_maker
# schema_table: conformed_data_07.tc00104rv_kpj_maker

def generate_insert_sql(table_name,data_source):
    schema_table = 'conformed_data_07.' + table_name
    value_list = data_source.split("\t")
    result = "INSERT INTO " + schema_table + " VALUES ("
    for i,v in enumerate(value_list):
        if (v.upper() == 'NULL'):
            str_value = v
        else:
            str_value = '\'' + v +'\''
        result = result + str_value
        if (i < len(value_list) - 1):
            result = result + ','
    return result + ');'

# 输入方法参数
# tc00015rv_local_manufacturer
# tc00104rv_kpj_maker
table_name = 'tc00104rv_kpj_maker'

need_format_str = 'sys_cd_06	makr_cd_06	makr_nk_06	20	PPPPPP	20221001_jc00076rv_kpj_local_manufacturer	2022-11-10 21:51:33	jc00076rv_kpj_local_manufacturer'

value = generate_insert_sql(table_name, need_format_str)

print('*************************')
print()
print(value)
print()
print('*************************')