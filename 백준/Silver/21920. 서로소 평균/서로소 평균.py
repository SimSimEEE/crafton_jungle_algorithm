import math
n = int(input())
A = list(map(int, input().split()))
x = int(input())
cnt = 0
result = 0

for a in A:
    if math.gcd(a, x) == 1:
        cnt += 1
        result += a
print(result/cnt)