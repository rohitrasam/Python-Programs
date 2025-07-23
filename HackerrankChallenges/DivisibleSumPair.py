s = input().split(" ")
n = int(s[0])
k = int(s[1])
count = 0
arr = list(map(int, input().split(" ")))
for i in range(n-1):
    for j in range(i+1, n):
        if (arr[i] + arr[j]) % k == 0:
            count += 1
print(count)
