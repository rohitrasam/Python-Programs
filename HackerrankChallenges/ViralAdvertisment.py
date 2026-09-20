import math as m
if __name__ == '__main__':
    n = int(input())
    likes = 0
    likesList = []
    shares = 0
    recipients = 5
    for i in range(n):
        likes = m.floor(recipients / 2)
        likesList.append(likes)
        shares = likes * 3
        recipients = shares

    print(sum(likesList))
