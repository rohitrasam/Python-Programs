def workbook(n, k, a):
    page = {}
    page_nos = 1
    for i in a:
        page[page_nos] = []
        for j in range(1, i+1):
            page[page_nos] += [j]
            if len(page[page_nos]) >= k:
                page_nos += 1
                page[page_nos] = []
        page_nos += 1
        if i % k == 0:
            page_nos -= 1

    counter = 0
    for key in page.keys():
        if key in page[key]:
            counter += 1

    return counter


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = workbook(n, k, arr)
    print(ans)


    # page_nos = {}
    # i = 1
    # j = 0
    # while j < n:
    #     fact = arr[j] % k
    #     if fact != 0:
    #         end = arr[j] - (arr[j]//k)
    #         if arr[j] < k:
    #             page_nos[i] = list(range(1, end+1))
    #             i += 1
    #             j += 1
    #         else:
    #             page_nos[i] = list(range(1, end+1))
    #             page_nos[i+1] = list(range(end+1, arr[j]+1))
    #             i += 2
    #             j += 1
    #     elif fact == 0:
    #         page_nos[i] = list(range(1, (arr[j] // 2) + 1))
    #         page_nos[i+1] = list(range((arr[j] // 2)+1, arr[j]+1))
    #         i += 2
    #         j += 1
    #
    # print(page_nos)
    # print(page_nos[1])
