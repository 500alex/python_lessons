s = ["rgvd", "rtve", "rtvec", "rcwertcr"]
for i in s:
    print(i)
print()
for i in range(len(s)):  # len() - возвращает "длину" аргумента (т.е. кол-во элементов в нем)
    print(s[i])
# enumerate() - возвращает кортеж, в котром первым элементом явдяется индекс элемента аргумента, а вторым - сам элемент
for ind, elem in enumerate(s):
    print(ind, elem)