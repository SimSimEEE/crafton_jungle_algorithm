def solution(arr, n):
    for i in range(len(arr)-1, -1, -2):
        print(i)
        arr[i] += n
    return arr