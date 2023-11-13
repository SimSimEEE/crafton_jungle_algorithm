n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(n)]

def reverse_3x3(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = '1' if a[i][j] == '0' else '0'
            
if n < 3 or m < 3:
    print(-1 if a != b else 0)
    exit()
    
result = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            result += 1
            reverse_3x3(i, j)

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print(-1)
            exit()

print(result)
