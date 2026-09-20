import sys

num=int(input("Enter a unumber: "))
if 99 < num < 999:
    print('It is a 3 digit num')
elif 999 < num < 9999:
    print('It is a 4 digit num')
else:
    print('not in range')

# argv
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x + y
print(z)
