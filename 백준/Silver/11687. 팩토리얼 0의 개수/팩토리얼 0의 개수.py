m = int(input())
start = 1
end = m * 5
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    tmp = mid
    while tmp >= 5:
        cnt += tmp // 5
        tmp //= 5
    if cnt < m:
        start = mid + 1
    else:
        if cnt == m:
            result = mid
        end = mid - 1
print(result if result else -1)