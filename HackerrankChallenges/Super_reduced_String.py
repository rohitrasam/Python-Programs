from this import d


def superReducedString(string):
    i = 0
    alpha_list = list(string)
    while i < len(alpha_list)-1:
        if len(alpha_list) == 0:
            break
        if alpha_list[i] == alpha_list[i+1]:
            del alpha_list[i]
            del alpha_list[i]
            i = 0
        else:
            i += 1
    return ''.join(alpha_list) if len(alpha_list) > 0 else "Empty String"


if __name__ == '__main__':
    s = input()
    ans = superReducedString(s)
    print(ans)
