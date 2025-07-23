# def average(array):
#     set1 = set(array)
#     sum1 = 0
#     for i in set1:
#         sum1 += i
#     return sum1 / len(set1)
#     # your code goes here
#
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)


# m = int(input())
# M1 = input().split(" ")
# n = int(input())
# N1 = input().split(" ")
# M = set(map(int, M1))
# N = set(map(int, N1))
#
# diff = sorted(list(M.symmetric_difference(N)))
# for k in diff:
#     print(k)


n = int(input())
countries_list = [input() for i in range(n)]
countries_set = set(countries_list)
print(len(countries_set))

