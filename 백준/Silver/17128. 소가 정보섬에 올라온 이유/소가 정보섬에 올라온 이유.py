n, q = map(int, input().split())
a = list(map(int, input().split()))
Q = list(map(int, input().split()))
A = [1] * n
for i in range(n):
    for j in range(4):
        idx = i + j
        if idx >= n:
            idx -= n
        A[i] *= a[idx]
As = sum(A)
for i in Q:
    for j in range(i-4, i):
        A[j] = -A[j]
        As += A[j]*2
    print(As)
