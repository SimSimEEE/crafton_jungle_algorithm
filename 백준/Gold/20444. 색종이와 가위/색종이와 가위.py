n, k = map(int, input().split())

s = 0
e = n // 2 + 1

result = "NO"
while s <= e:
    mid = (s + e) // 2
    if (mid + 1) * (n - mid + 1) == k:
        result = "YES"
        break
    if s == e:
        break
    if (mid + 1) * (n - mid + 1) > k:
        e = mid - 1
    else:
        s = mid + 1

print(result)
