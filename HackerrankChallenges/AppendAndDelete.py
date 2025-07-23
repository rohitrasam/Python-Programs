def appendAndDelete(s, t, k):
    count = 0
    for i, j in zip(s, t):
        if i == j:
            count += 1
        else:
            break

    t_len = len(s) + len(t)
    # Case 1-: t_len <= 2*count + k : YES
    # Case 2-: t_len%2 == k%2
    # Case 3-: t_len < k

    # Case1 and Case2 or Case3

    if t_len <= 2*count + k and (t_len % 2 == k % 2 or t_len < k):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input())

    appendAndDelete(s, t, k)
