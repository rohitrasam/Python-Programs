i = 1
while i <=4:
    j = 1
    while j <= i:
        print(j,end =" ")
        j += 1
    i += 1
    print()

for i in range(5):
    for j in range(1,5-i):
        print(j,end =" ")
    print()
