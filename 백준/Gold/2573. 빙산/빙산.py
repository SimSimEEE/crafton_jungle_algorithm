import sys
from collections import deque

def bfs(start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if iceberg[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def melt():
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    melts = []
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0:
                cnt = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m and iceberg[nx][ny] == 0:
                        cnt += 1
                melts.append((i, j, cnt))

    for x, y, cnt in melts:
        iceberg[x][y] = max(iceberg[x][y] - cnt, 0)

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    years = 0

    while True:
        cnt = 0
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if iceberg[i][j] > 0 and not visited[i][j]:
                    bfs((i, j), visited)
                    cnt += 1
        if cnt > 1:
            print(years)
            break
        if cnt == 0:
            print(0)
            break
        melt()
        years += 1
