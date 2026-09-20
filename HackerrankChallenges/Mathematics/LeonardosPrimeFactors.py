import math


def isPrime(num: int):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def primeCount(n: int):
    # Write your code here
    if n == 1:
        return 0
    
    mul = 1
    count = 0
    for i in range(2, math.ceil(n**0.5)+1):
        if isPrime(i):
            mul *= i
            if mul > n:
                break
            else:
                count += 1
    
    return count


if __name__ == '__main__':

    print(primeCount(1))
    print(primeCount(2))
    print(primeCount(3))
    print(primeCount(500))
    print(primeCount(5000))
    print(primeCount(10000000000))