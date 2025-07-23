def caesarCipher(s: str, k: int):
    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    k = k % 26
    capital_ = capital[k:] + capital[:k]
    alpha_ = alpha[k:] + alpha[:k]
    symbols = ['-', "'", '/', ',', '.', '?', '"', '`', 
                 '~', '!', '@', '#', '$', '%', ':', ';' 
                 '^', '&', '*', '(', ')', '_', '>', '<', 
                 '-', '+', '=', '{', '}', '[', ']', '|',
                 '1', '2', '3', '4', '5', '6', '7', '\\',
                 '8', '9', '0']

    for i in s:
        if i in symbols:
            encrypted += i
        elif i.isupper():
            encrypted += capital_[capital.index(i)]
        else:
            encrypted += alpha_[alpha.index(i)]
    
    return encrypted

    



if __name__ == '__main__':
    n = int(input())
    s = input()
    k = int(input())

    ans = caesarCipher(s, k)
    print(ans)






