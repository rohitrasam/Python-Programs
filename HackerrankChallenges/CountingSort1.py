def countingSort(arr):
    # Write your code here
    output = []
    count = [0] * 100
    for i in arr:
        count[i] += 1
    
    for j in range(len(count)):
        for k in range(count[j]):
            output.append(j)
    
    return " ".join(list(map(str, output)))


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    print(countingSort(A))

