t = int(input())
for _ in range(t):
    a, b = input().split(" ")
    a = [char for char in a]
    b = [char for char in b]
    a.sort()
    b.sort()
    for num1, num2 in zip(a, b):
        if int(num1) != int(num2):
            print("not recycled pair")
            break
    else:
        print("recycled pair")


