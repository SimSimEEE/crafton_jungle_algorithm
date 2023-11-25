n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
start = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            start = [i, j]
            break
        
def bfs():
    q = [[start[0], start[1]]]
    visited[start[0]][start[1]] = True
    global cnt
    cnt = 0
    while q:
        x, y = q.pop(0)
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 'X':
                visited[nx][ny] = True
                if graph[nx][ny] == 'P':
                    cnt += 1
                q.append([nx, ny])
    return cnt if cnt else 'TT'

print(bfs())