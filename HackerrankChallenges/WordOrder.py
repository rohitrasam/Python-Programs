# n = int(input())
# count = 0
# words = [input() for i in range(n)]
# words_set = set(words)
# count_list = [1 for x in range(len(words)-1)]
# for i in range(len(words)-1):
#     for j in words_set:
#         if words[i] == j:
#             count += 1
#             count_list[i] += 1
#         else:
#             count_list[i] = 1
#
# print(len(words_set))
# print(*sorted(count_list, reverse=True))

from collections import OrderedDict
words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1

print(len(words))
print(*words.values())
