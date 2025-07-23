
def candies(n, arr):
    number_candies = []
    number_candies.append(1)

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            number_candies.append(number_candies[i-1] + 1)
        else:
            number_candies.append(1)

    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1] and number_candies[i] <= number_candies[i+1]:
            number_candies[i] = number_candies[i+1] + 1
    
    return sum(number_candies)


n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input().strip()))

result = candies(n, arr)
print(result)