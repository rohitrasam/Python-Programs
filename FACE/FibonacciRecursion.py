# import timeit
# from statistics import mean

# y1 = """
# def fib(n, arr):
#     if arr[n] != -1:
#         return arr[n]
#     else:
#         arr[n] = fib(n-1, arr) + fib(n-2, arr)
#         return arr[n]
# y = fib(50, [-1 if i > 1 else i for i in range(50 + 1)])"""


# if __name__ == '__main__':

#     list1 = [timeit.timeit(stmt=y1, number=1000)]
#     print(mean(list1))


def fib(n):

    if n >= 100:
        return "Out of range"
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)


print(fib(15))
