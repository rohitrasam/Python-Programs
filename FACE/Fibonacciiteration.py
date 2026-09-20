import timeit
from statistics import mean

x1 = """
def func(n):    
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr
x = func(50)"""

if __name__ == '__main__':

    list1 = [timeit.timeit(stmt=x1, number=1000)]

    print(mean(list1))
