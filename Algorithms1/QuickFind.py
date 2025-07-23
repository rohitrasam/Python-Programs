def connected(p, q, iid):
    a = iid[p]
    b = iid[q]
    if a == b:
        return True
    return False


def union(p, q, iid):
    pid = iid[p]
    qid = iid[q]
    for i in range(len(iid)):
        if iid[i] == pid:
            iid[i] = qid
    print(iid)


if __name__ == "__main__":
    n = int(input())
    iid = [i for i in range(n)]
    print(iid)
    while True:
        p = int(input())
        q = int(input())
        if not connected(p, q, iid):
            union(p, q, iid)
            print("{} {}".format(p, q))

