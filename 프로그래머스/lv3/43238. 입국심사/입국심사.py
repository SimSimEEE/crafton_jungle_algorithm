def solution(n, times):
    answer = 0
    times.sort()
    low = 1
    high = times[-1] * n
    while low <= high:
        mid = (low + high) // 2
        tmp = 0
        for time in times:
            tmp += mid // time
        if tmp >= n:
            high = mid - 1 
            answer = mid 
        else:
            low = mid + 1 
    return answer