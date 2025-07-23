def alternate(string):
    combo = list(set(string))
    max_length = 0
    pairs = []

    i = 0
    j = i+1

    while i < len(combo)-1:
        pairs.append((combo[i], combo[j]))
        if j == len(combo)-1:
            i += 1
            j = i + 1
        else:
            j += 1
        
    for pair in pairs:
        temp = [char for char in string if char in pair]
        for idx in range(len(temp)-1):
            if temp[idx] == temp[idx+1]:
                break
        else:
            if len(temp) > max_length:
                max_length = len(temp)

    return max_length



if __name__ == '__main__':

    l = int(input())
    s = input()

    print(alternate(s))