def solution(arr):
    cache = [[None] * len(arr) for _ in range(2)]
    cache[0][0] = arr[0]
    cache[1][0] = -arr[0]
    for i in range(1, len(arr)):
        cache[0][i] = max(0, cache[0][i-1]) + arr[i] * ((-1)**(i%2))
        cache[1][i] = max(0, cache[1][i-1]) + arr[i] * ((-1)**((i+1)%2))
    mp = max(cache[0])
    mn = max(cache[1])
    return max(mp, mn)