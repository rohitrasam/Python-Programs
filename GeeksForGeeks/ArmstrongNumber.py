def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        ret = power(x, y // 2)
        ret1 = power(x, y // 2)
        return ret * ret1
    ret = x * power(x, y // 2)
    ret1 = power(x, y // 2)
    return ret * ret1


def order(x):

    count = 0
    while x != 0:
        count += 1
        x //= 10

    return count


def isArmStrong(x):
    digit = order(x)
    temp = x
    sum1 = 0
    while temp != 0:
        r = temp % 10
        sum1 += power(r, digit)
        temp //= 10

    return 'It is an armstrong number' if sum1 == x else 'It is not an armstrong number'


if __name__ == '__main__':

    while True:
        n = int(input('Enter a number to check if it is an armstrong number or not: '))

        print(isArmStrong(n))








    # while True:
    #     n = input('Enter a number to check if it is an armstrong number or not: ')
    #     d = len(n)
    #     sum1 = 0
    #     for i in n:
    #         sum1 += int(i)**d
    #
    #     if sum1 == int(n):
    #         print('{} = {} yes it is an armstrong number'.format(sum1, n))
    #     else:
    #         print('{} != {} therefore it is not an armstrong number'.format(sum1, n))
