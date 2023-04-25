from collections import deque
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(input()))
    
drow = [-1, 1, 0, 0]
dcol = [0, 0, 1, -1]

distance = [[0]*m for _ in range(n)]

queue = deque([])

def bfs(Drow,Dcol):
    while queue:
        row, col = queue.popleft()
        if maze[Drow][Dcol] == 'S':
            return distance[Drow][Dcol]
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < n and 0 <= ncol < m:
                if maze[row][col] == 'S':
                    if maze[nrow][ncol] == 'D' or maze[nrow][ncol] == '.':
                        maze[nrow][ncol] = 'S'
                        queue.append([nrow, ncol])
                        distance[nrow][ncol] = distance[row][col] + 1
                elif maze[row][col] == '*':
                    if maze[nrow][ncol] == 'S' or maze[nrow][ncol] == '.':
                        queue.append([nrow, ncol])
                        maze[nrow][ncol] = '*'

    return "KAKTUS"

Drow, Dcol = 0, 0
for i in range(n):
    for j in range(m):
        if maze[i][j] == 'S':
            queue.append([i, j])
        elif maze[i][j] == 'D':
            Drow,Dcol = i,j

for i in range(n):
    for j in range(m):
        if maze[i][j] == '*':
            queue.append([i, j])

print(bfs(Drow,Dcol))