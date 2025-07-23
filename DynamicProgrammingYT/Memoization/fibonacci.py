# Time complexity -: O(n)
# Space complexity -: O(n)

def fib(n, memo=None):
    if memo is None:
        memo = {}
    if len(memo) != 0 and n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


print(fib(6))   # 8
print(fib(7))   # 13
print(fib(8))   # 21
print(fib(50))  # 12586269025
