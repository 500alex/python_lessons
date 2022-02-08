# словарь {} dict() - как список, но индексы задаются самостоятельно
# {key1: value1, key2: value2,... }
Technics = {'smartphone': ['iphone 1', 'iphone 6s+', 'iphone 7'], 'graphic cards': ['rtx2080', 'rtx2070', 'rtx2000']}
# в качестве ключей необходимо использовать только неизменяемые обЪекты, а в качестве значениний - любые
print(Technics)
print(Technics['smartphone'])
for i in Technics:
    print(i)
    print(Technics[i])
Technics['tey8'] = ['черный',"красный","ягодный"]
print(Technics)