def gemstones(rocks: list[str]):
    # Write your code here
    gemstones = 0
    for mineral in range(ord('a'), ord('z')+1):
        count = 0
        for rock in rocks:
            if chr(mineral) in rock:
                count += 1
        if count == len(rocks):
            gemstones += 1
    return gemstones


if __name__ == '__main__':
    n = int(input())

    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    
    result = gemstones(arr)
    print(result)