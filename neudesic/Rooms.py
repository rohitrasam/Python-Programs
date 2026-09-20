if __name__ == '__main__':
    t = int(input())
    vow = "AEIOUaeiou"
    rooms = []
    for i in range(t):
        room = input()
        rooms.append(room)

    for i, r in enumerate(rooms):
        if r[len(r)-1] == "y":
            print("Case #{}: {} is commanded by awesome techies.".format(i+1, r))
        elif r[0] not in vow:
            print("Case #{}: {} is commanded by dynamic directors.".format(i+1, r))
        elif r[0] in vow:
            print("Case #{}: {} is commanded by cool HRs.".format(i+1, r))