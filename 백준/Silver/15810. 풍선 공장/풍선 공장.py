n, m = map(int, input().split())
a = list(map(int, input().split()))
start, end = 1, max(a) * m
while start <= end:
    mid = (start + end) // 2
    s = 0
    for i in a:
        s += mid // i
    if s >= m:
        end = mid - 1
    else:
        start = mid + 1
print(start)
