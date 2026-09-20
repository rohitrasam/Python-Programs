from itertools import permutations


def biggerIsGreater(word):
    result = ''
    n = len(word)
    word = list(word)

    i = n-2

    while i >=0 and word[i] >= word[i+1]:
        i -= 1

    if i == -1:
        result = 'no answer'
    else:
        j = n-1
        while j >= i and word[j] <= word[i]:
            j -= 1
        
        word[i], word[j] = word[j], word[i]

        word = ''.join(word)
        result = word[:i+1] + word[i+1:][::-1]
    
    return result


if __name__ == '__main__':

    T = int(input())

    for _ in range(T):
        w = input()

        result = biggerIsGreater(w)
        print(result)