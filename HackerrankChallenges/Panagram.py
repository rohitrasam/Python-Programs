def panagram(string: str):
    alpha = set(string.lower())
    print(alpha)
    return 'panagram' if len(alpha) == 26 else 'not panagram'



if __name__ == '__main__':
    s = input()
    panagram(s)
