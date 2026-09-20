"""
canSum(targetSum, numbers) that takes in a targetSum and an array of numbers as argument.

Function should return a boolean indicating whether or not it is possible to generate
the targetSum using the numbers from the array.

You may use the element of the array as many times as you want
You may assume that all the input numbers are positive.
"""


def canSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        rem = targetSum - num
        if canSum(rem, numbers, memo):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(canSum(7, [2, 3]))        # True
print(canSum(7, [5, 3, 4, 7]))  # True
print(canSum(7, [2, 4]))        # False
print(canSum(8, [2, 3, 5]))     # True
print(canSum(300, [7, 14]))       # False
