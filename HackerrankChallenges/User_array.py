from array import *
arr = array('i', [])
n = int(input('Enter the size of the array: '))
for i in range(n):
    x = int(input('Enter the next value: '))
    arr.append(x)

for j in range(n):
    print(arr[j], end=" ")
print()
search = int(input('Enter the search value: '))
k = 0
for e in arr:
    if e == search:
        print('The value is at index', k)
        break
    k += 1

print(arr.index(search))
