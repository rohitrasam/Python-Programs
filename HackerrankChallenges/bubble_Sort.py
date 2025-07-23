n = int(input('Enter the size of the array: '))
a = list(map(int, input().split()))
count = 0
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            count += 1
print(a)
