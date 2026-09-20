from cgitb import small


def toys(weights: list[int]) -> int:

    # Optimized solution
    cost = 0

    weights.sort()
    current = weights[0]

    for i in range(1, len(weights)):
        if weights[i] > current + 4:
            cost += 1
            current = weights[i]
    
    return cost


    # i = 0
    # while i < len(weights):
    #     smallest = weights[i]
    #     container = [smallest]
    #     for j in range(i+1, len(weights)):
    #         if weights[j] <= smallest + 4:
    #             container.append(weights[j])
    #         else: 
    #             break
    #     counter += 1
    #     i += len(container)

    # return counter

if __name__ == '__main__':
    n = int(input())

    w = list(map(int, input().split()))

    toys(w)