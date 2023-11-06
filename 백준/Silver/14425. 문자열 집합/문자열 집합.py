n, m = map(int, input().split())
s = list(input() for _ in range(n))
result = 0
for _ in range(m):
    if input() in s:
        result += 1
print(result)