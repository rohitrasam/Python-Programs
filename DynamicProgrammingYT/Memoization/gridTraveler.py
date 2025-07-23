# Move from top left corner to the bottom right corner.
# You may only move down or right.
# In how many ways can you travel to the goal on a grid with dimensions m * n?

# Brute Force: 1. Time Complexity: O(2^(n+m))
#              2. Space Complexity: O(n+m)

# Memoized: 1. Time Complexity: O(m*n)
#           2. Space Complexity: O(m+n)


def traveler(m, n, memo={}):
    key = '{}, {}'.format(m, n)
    # are the args in the memo
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = traveler(m - 1, n, memo) + traveler(m, n - 1, memo)
    return memo[key]


print(traveler(1, 1))    # 1
print(traveler(2, 3))    # 3
print(traveler(3, 2))    # 3
print(traveler(3, 3))    # 6
print(traveler(18, 18))  # 2333606220
print(traveler(4, 3))    # 10
