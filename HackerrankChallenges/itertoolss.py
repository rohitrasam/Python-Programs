from itertools import product, permutations, combinations
# A = [int(x) for x in input().split()]
# B = [int(y) for y in input().split()]
# print(*product(A, B))

# s = input().split(" ")
# r = int(s[len(s)-1])
# permutes = list(permutations(sorted(s[0]), r))
# for i in permutes:
#     for j in i:
#         print(j, end="")
#         # print(*["".join(i)])
#     print()


s = input().split(" ")
r = int(s[len(s) - 1])
for L in range(1, r+1):
    for i in combinations(sorted(s[0]), L):
        print("".join(i))
