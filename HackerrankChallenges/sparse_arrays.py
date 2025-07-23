
def matchingStrings(strings: list[str], queries: list[str]):

    ans = []

    for query in queries:
        counter = 0
        for string in strings:
            if query == string:
                counter += 1
        ans.append(counter)

    return ans

if __name__ == '__main__':

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    print(res)