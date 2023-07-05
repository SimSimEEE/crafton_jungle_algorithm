n = int(input())
graph = [['*']*n for _ in range(n)]

def delete_star(n, x, y):
    if n == 1:
        return
    for i in range(x + n//3, x + 2*n//3):
        for j in range(y + n//3, y + 2*n//3):
            graph[i][j] = " "
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                delete_star(n//3, x + i * (n//3), y + j * (n//3))

delete_star(n, 0, 0)
for i in range(n):
    print(*graph[i], sep="")