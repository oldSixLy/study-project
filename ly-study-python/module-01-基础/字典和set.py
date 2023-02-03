# dict键-值（key-value）存储
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d.get('aaa', '没有对应key'))
print('Bob' in d)
print(d)
d.pop('Tracy')
print(d)
print('-------------------------------------------------')
# set key的集合
s = set(['key1', 'key2', 'key3', 'key1'])
print(s)
s.add('key888')
print(s)
s.remove('key888')
print(s)