def invert(texts):
    for i, text in enumerate(texts):
        text = text.split()
        print("Case #{}: {}".format(i+1, " ".join(text[::-1])))


if __name__ == '__main__':
    t = int(input())
    texts = []
    for _ in range(t):
        s = input()
        texts.append(s)

    invert(texts)
