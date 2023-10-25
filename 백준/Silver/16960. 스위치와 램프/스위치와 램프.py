n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
switch = [0] * m
for a in A:
    for i in range(1, len(a)):
        switch[a[i] - 1] += 1
for a in A:
    lamp = switch[:]
    for i in range(1, len(a)):
        lamp[a[i] - 1] -= 1
    if 0 not in lamp:
        print(1)
        exit(0)
else:
    print(0)