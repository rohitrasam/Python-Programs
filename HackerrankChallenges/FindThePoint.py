def findPoint(px, py, qx, qy):
    rx = (2 * qx) - px
    ry = (2 * qy) - py
    print(str(rx) + " " + str(ry))


n = int(input())

for n_itr in range(n):
    pxpyqxqy = input().split()
    px = int(pxpyqxqy[0])
    py = int(pxpyqxqy[1])
    qx = int(pxpyqxqy[2])
    qy = int(pxpyqxqy[3])
    findPoint(px, py, qx, qy)
