# from itertools import groupby
#
# groups = []
# unique_keys = []
#
# string = input()
#
# for i, j in groupby(string):
#     groups.append(tuple(j))
#
# for index, k in enumerate(groups):
#     unique_keys.append((groups[index].count(groups[index][0]), int(groups[index][0])))
#
# print(*unique_keys)

a = 23
b = 2
print(a >> b)
print(b << a)
