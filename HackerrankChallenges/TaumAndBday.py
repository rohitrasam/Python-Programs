def taumBday(b, w, bc, wc, z):
    print(min(b*bc + w*wc, bc*(w+b) + w*z, wc*(w+b) + b*z))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        b, w = map(int, input().split())
        bc, wc, z = map(int, input().split())

        taumBday(b, w, bc, wc, z)