n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = float('inf')
point1 = 0
point2 = 0
sum = a[0]
while point1 < n:
    if sum >= s:
        ans = min(ans, point2 - point1 + 1)
        sum -= a[point1]
        point1 += 1
    else:
        point2 += 1
        if point2 == n:
            break
        sum += a[point2]
print(ans if ans != float('inf') else 0)
