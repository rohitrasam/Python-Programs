from collections import Counter


# a word can be a palindrome iff there is one letter with odd count

def gameOfThrone(string):

    counts = Counter(string)
    n_odds = 0

    for values in counts.values():
        if values % 2 == 1:
            n_odds += 1
            if n_odds > 1:
                return False

    return True



if __name__ == '__main__':

    s = input()

    print(gameOfThrone(s))