
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b


def get_gcd(n1, n2):
    if n2 == 0:
        return n1
    return get_gcd(n2, n1 % n2)


def get_lcm(n1, n2):
    return n1 * n2 / get_gcd(n1, n2)


def getTotalX(a, b):
    multiple = 0
    counter = 0

    lcm = a[0]
    for item in a:
        lcm = get_lcm(lcm, item)

    gcd = b[0]
    for item in b:
        gcd = get_gcd(gcd, item)

    while multiple <= gcd:
        multiple += lcm

        if gcd % multiple == 0:
            counter += 1

    return counter


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
