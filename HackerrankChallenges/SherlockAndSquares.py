from math import sqrt, floor, ceil


def squares(a, b):
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        a, b = input().split()

        print(squares(int(a), int(b)))