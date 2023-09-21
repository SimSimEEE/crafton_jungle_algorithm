def solution(arr):
    ln = len(arr)
    for i in range(ln):
        for j in range(ln):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1