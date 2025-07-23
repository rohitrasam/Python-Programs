
def weightedUniformStrings(string: str, q: list[int]):
    vals = {}
    weight = 0
    for idx in range(len(string)):
        if idx == 0 or s[idx] != s[idx-1]:
            weight = ord(string[idx]) - ord('a') + 1 
        else:
            weight += ord(string[idx]) - ord('a') + 1
        vals[weight] = 1
    
    ans = []
    for value in q:
        ans.append('Yes' if value in vals.keys() else 'No')
    
    print(ans)
        
    

if __name__ == '__main__':
    s = input()

    query_count = int(input())
    queries = []

    for _ in range(query_count):
        queries_item = int(input().strip())
        queries.append(queries_item)
    
    result = weightedUniformStrings(s, queries)


# s = input()
# t = int(input())
# w = 0
# dic = {}
# for i in range(0, len(s)):
#         if i == 0 or s[i] != s[i-1]:
#             w = ord(s[i]) - ord('a') + 1
#         else:
#             w = w + ord(s[i]) - ord('a') + 1
#         dic[w] = 1

# print(dic)