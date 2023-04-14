import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(1, 1 << N):
    result = 0
    for j in range(N):
        if i & 1 << j == 0:
            continue
        result += A[j]
    if result == S:
        count += 1
print(count)