from itertools import combinations 
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
viruses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            viruses.append((i, j))
            graph[i][j] = 0
min_cnt = 1e9
for i in combinations(viruses, m):
    i = deque(i)
    visited = [[0] * n for _ in range(n)]
    for x, y in i:
        visited[x][y] = 1
    cnt = 0
    while i:
        ln = len(i)
        cnt += 1
        for _ in range(ln):
            x, y = i.popleft()
            visited[x][y] = 1
            for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    i.append((nx, ny))
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 0 and not visited[x][y]:
                cnt = 1e9
                break
    min_cnt = min(min_cnt, cnt)
print(min_cnt - 1 if min_cnt != 1e9 else -1)