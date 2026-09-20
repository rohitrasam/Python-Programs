import math as m


def encryption(s):
    L = len(s)
    col = m.ceil(m.sqrt(L))
    j = 0
    p = []
    for _ in range(col):
        p.append(s[j::col].rstrip())
        j += 1
    print(*p)


if __name__ == '__main__':
    s = input()

    encryption(s)