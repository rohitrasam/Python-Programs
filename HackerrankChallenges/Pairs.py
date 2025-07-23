"""My solution"""
# def pairs(arr, k):
#     counter = 0
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             if abs(arr[i] - arr[j]) == k:
#                 counter += 1
#
#     print(counter)
#
#
# if __name__ == '__main__':
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     pairs(arr, k)


"""Optimized Solution"""


def pairs(a, k):
    # a is the list of numbers and k is the difference value
    a.sort()
    left = 0
    right = 1
    answer = 0
    while right < len(a):
        val = a[right]-a[left]
        if val == k:
            answer += 1
            left += 1
            right += 1
        elif val < k:
            right += 1
        else:
            left += 1
            if left == right:
                right += 1

    return answer


# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size = a[0]
    _k = a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b, _k))


"""Even more optimized solution"""
# a = list(map(int, input().split()))
# k = int(input())
# print(len(set(a) & set(x + k for x in a)))
