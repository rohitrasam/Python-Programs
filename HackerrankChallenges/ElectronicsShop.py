def getMoneySpent(keyboards, drives, b):
    maximum = 0
    for i in keyboards:
        for j in drives:
            sum1 = i + j
            if maximum < sum1 < b:
                maximum = sum1
    if sum1 > b:
        return -1
    else:
        return maximum


bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().split()))
drives = list(map(int, input().split()))

moneySpent = getMoneySpent(keyboards, drives, b)
print(moneySpent)
