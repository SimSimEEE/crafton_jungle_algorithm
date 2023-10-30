n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs_num(x, y, i_num):
    queue = []
    graph[x][y] = i_num
    queue.append((x, y))
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and graph[new_x][new_y] == 1:
                graph[new_x][new_y] = i_num
                queue.append((new_x, new_y))


def bfs_bridge(i_num):
    queue = []
    dist = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == i_num:
                queue.append((i, j))
                dist[i][j] = 0

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                if graph[new_x][new_y] and graph[new_x][new_y] != i_num:
                    return dist[x][y]
                if graph[new_x][new_y] == 0 and dist[new_x][new_y] == -1:
                    dist[new_x][new_y] = dist[x][y] + 1
                    queue.append((new_x, new_y))

    return float('inf')


i_num = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            i_num += 1
            bfs_num(i, j, i_num)
result = float('inf')
for i in range(1, i_num):
    result = min(result, bfs_bridge(i))
print(result)
