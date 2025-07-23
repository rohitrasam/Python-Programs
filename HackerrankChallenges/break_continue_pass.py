x = int(input("How many candies do you want?\n"))
i = 1
limit = 10
while i <= x:
    if x > limit:
        print('Sorry we are out of candies :(')
        break
    print("Candy")
    i += 1
print("Thank you")

for h in range(1, 11):
    if  h % 3 == 0:
        continue
    print(h)

for i in range(1, 11):
    if i % 2 != 0:
        pass
        print('hi')
    else:
        print(i)
