n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)] 
for _ in range(r):
    for i in range(min(n, m) // 2):
        t = a[i][i]
        for j in range(i + 1, m - i): a[i][j - 1] = a[i][j]
        for j in range(i + 1, n - i): a[j - 1][m - i - 1] = a[j][m - i - 1]
        for j in range(m - i - 2, i - 1, -1): a[n - i - 1][j + 1] = a[n - i - 1][j]
        for j in range(n - i - 2, i - 1, -1): a[j + 1][i] = a[j][i]
        a[i + 1][i] = t
for i in a:
    for j in i: print(j, end=' ')
    print()