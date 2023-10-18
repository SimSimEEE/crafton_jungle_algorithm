n, m, k = map(int, input().split())
def combination(n, m):
    if n < m:
        return 0
    p, c = 1, 1
    for i in range(m):
        p *= n - i
        c *= i + 1
    return p // c
lotto = 0
for i in range(k, m + 1):
    if n - m < m - i:
        continue
    lotto += combination(m, i) * combination(n - m, m - i)
print(lotto / combination(n, m))