n, k = map(int,input().split())
result = 0
for i in range(1, k + 1):
    result = max(result, int(str(n * i)[::-1]))
print(result)