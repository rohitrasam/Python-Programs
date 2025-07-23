def designerPdfViewer(h, word):
    m = max(h)
    length = len(word)
    return m * length


if __name__ == '__main__':
    h = list(map(int, input().split()))
    word = input()
    print(designerPdfViewer(h, word))
