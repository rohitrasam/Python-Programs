from collections import Counter

n = int(input())
sizes = list(map(int, input().split()))
num_customers = int(input())
quantity = Counter(sizes)
sum1 = 0
for i in range(num_customers):
    a, b = map(int, input().split())
    if a in quantity.keys() and int(quantity.get(a)) > 0:
        quantity[a] = quantity.get(a) - 1
        sum1 += b

print(sum1)
