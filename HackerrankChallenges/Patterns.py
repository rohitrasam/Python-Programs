# Pattern 1
print('Pattern 1')
for i in range(1, 6):
    for j in range(1, 6):
        print('*', end=' ')
    print()
print()

# Pattern 2
print("Pattern 2")
for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=' ')
    print()
print()

# Pattern 3
print("Pattern 3")
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=' ')
    print()
print()

# Pattern 4
print("Pattern 4")
for i in "ABCDE":
    for j in "ABCDE":
        print(i, end=' ')
    print()
print()

# Pattern 5
print('Pattern 5')
for i in "ABCDE":
    for j in "ABCDE":
        print(j, end=' ')
    print()
print()

# Pattern 6
print("Pattern 6")
for i in range(5, 0, -1):
    for j in range(5, 0, -1):
        print(i, end=' ')
    print()
print()

# Pattern 7
print("Pattern 7")
for i in range(5, 0, -1):
    for j in range(5, 0, -1):
        print(j, end=' ')
    print()
print()

# Pattern 8
print("Pattern 8")
for i in "EDCBA":
    for j in "EDCBA":
        print(i, end=' ')
    print()
print()

# Pattern 9
print('Pattern 9')
for i in "EDCBA":
    for j in "EDCBA":
        print(j, end=' ')
    print()
print()

# Pattern 10
print("Pattern 10")
for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end=' ')
    print()
print()

# Pattern 11
print("Pattern 11")
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=' ')
    print()
print()

# Pattern 12
print("Pattern 12")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()

# Pattern 13
print("Pattern 13")
st = "ABCDE"
for i in st:
    for j in st[0:st.index(i)+1]:
        print(i, end=' ')
    print()
print()

# Pattern 14
print("Pattern 14")
for i in st:
    for j in st[0:st.index(i)+1]:
        print(j, end=' ')
    print()
print()

# Pattern 15
print('Pattern 15')
for i in range(1, 6):
    for j in range(5, i-1, -1):
        print('*', end=' ')
    print()
print()

# Pattern 16
print("Pattern 16")
for i in range(1, 6):
    for j in range(5, i-1, -1):
        print(i, end=' ')
    print()
print()

# Pattern 17
print("Pattern 17")
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()

# Pattern 18
print("Pattern 18")
for i in st:
    for j in st[st.index(i):]:
        print(i, end=' ')
    print()
print()

# Pattern 19
print("Pattern 19")
for i in range(5, 0, -1):
    for j in st[:i]:
        print(j, end=' ')
    print()
print()

# Pattern 20
print('Pattern 20')
for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=' ')
    print()
print()

# Pattern 21
print("Pattern 21")
for i in range(1, 6):
    for j in range(5, i-1, -1):
        print(j, end=' ')
    print()
print()

# Pattern 22
print("Pattern 22")
for i in st[::-1]:
    for j in range(0, st.index(i)+1):
        print(i, end=' ')
    print()
print()

# Pattern 23
print("Pattern 23")
for i in range(6, 1, -1):
    for j in st[-1:-i:-1]:
        print(j, end=' ')
    print()
print()

# Pattern 24
print("Pattern 24")
min_stars = 1
p_height = 5
p_space = p_height - 1
for i in range(p_height):
    for j in range(p_space, i, -1):
        print(" ", end=' ')
    for k in range(min_stars):
        print("*", end=' ')
    min_stars += 2
    print()
print()

for i in range(6):
    for j in range(6-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("*", end=" ")
    print()

for i in range(6):
    print(" " * (6-i-1) + "* " * (i+1))

# Pattern 24a
print("Pattern 24a")
min_stars = 1
p_height = 5
p_space = p_height - 1
for i in range(p_height):
    for j in range(p_space, i, -1):
        print(" ", end='')
    for k in range(min_stars):
        print("*", end=' ')
    min_stars += 1
    print()
print()
#
# Pattern 24b
print("Pattern 24b")
n = 5
px = n  # left print control
py = n  # right print control
for i in range(0, n):
    for j in range(n*2):
        if px <= j <= py:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    px -= 1
    py += 1
    print()
print()


for x in range(15):
    for y in range(15):
        if x == 0 or y == 0 or x == 15-1 or y == 15-1 or y == 15 - x - 1 or x == y or y == 15 // 2 or x == 15 // 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
print()
