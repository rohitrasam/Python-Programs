def maxSubArraySum(array):
    if len(array) == 1:
        return array[0]
    leftArray = array[0:len(array)//2]
    rightArray = array[len(array)//2:len(array)]
    maxRight = 0
    maxLeft = 0
    currentSum = 0
    for i in rightArray:
        currentSum += i
        if currentSum > maxRight:
            maxRight = currentSum

    currentSum = 0
    for j in leftArray:
        currentSum += j
        if currentSum > maxLeft:
            maxLeft = currentSum

    return max(maxSubArraySum(leftArray), maxSubArraySum(rightArray), maxRight + maxLeft)


arr = [4, -2, 2, 1, 2]
print(maxSubArraySum(arr))
