from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
tomato_box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
ripe_tomatoes = deque([])

moves = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato_box[i][j][k] == 1:
                ripe_tomatoes.append([i, j, k])

while ripe_tomatoes:
    i, j, k = ripe_tomatoes.popleft()
    for move in moves:
        ni = i + move[0]
        nj = j + move[1]
        nk = k + move[2]
        if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m and tomato_box[ni][nj][nk] == 0:
            ripe_tomatoes.append([ni, nj, nk])
            tomato_box[ni][nj][nk] = tomato_box[i][j][k] + 1

min_day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato_box[i][j][k] == 0:
                print(-1)
                exit()
            min_day = max(min_day,tomato_box[i][j][k])
else:
    print(min_day-1)