

def marsExploration(string: str):
    # Write your code here
    mistakes = 0
    for idx in range(0, len(string), 3):
        if string[idx] != 'S':
            mistakes += 1
        if string[idx+1] != 'O': 
            mistakes += 1
        if string[idx+2] != 'S':
            mistakes += 1

    return mistakes

if __name__ == '__main__':

    s = input()

    result = marsExploration(s)

    print(result)