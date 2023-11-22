from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
graph = [set() for _ in range((n + 1) * (m + 1))]  # Correct initialization of graph list
sum_list = []
def bfs(i, j, cnt):
    max_cnt = 1
    q = deque()
    q.append((i, j))
    visited[i][j] = cnt

    while q:
        x, y = q.popleft()
        binary = bin(board[x][y])[2:].zfill(4)  # 2진수로 변환

        # Define the possible directions (south, east, north, west)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and binary[directions.index((dx, dy))] == '0' and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = cnt
                max_cnt += 1
            else:
                if 0 <= nx < m and 0 <= ny < n:
                    if visited[nx][ny] != cnt:
                        graph[visited[nx][ny]].add(cnt)

    return max_cnt

cnt = 0
max_cnt = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            cnt += 1
            sum_list.append(bfs(i, j, cnt))
            max_cnt = max(max_cnt, sum_list[-1])

print(cnt, max_cnt, sep='\n')
max_cnt = 0
for i in range(1, cnt + 1):
    if len(graph[i]) != 0:
        for j in graph[i]:
            max_cnt = max(max_cnt, sum_list[i - 1] + sum_list[j - 1])
print(max_cnt)
