def solution(arr, queries):
    for s, e in queries:
        arr[s], arr[e] = arr[e], arr[s]
    return arr