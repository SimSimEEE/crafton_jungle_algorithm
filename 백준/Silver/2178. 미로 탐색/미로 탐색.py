from collections import deque
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

drow = [-1, 1, 0, 0]
dcol = [0, 0, 1, -1]

def bfs(row, col):
    visited = deque([[row, col]])
    while visited:
        row, col = visited.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < n and 0 <= ncol < m and maze[nrow][ncol] == 1:
                visited.append([nrow, ncol])
                maze[nrow][ncol] = maze[row][col] + 1

bfs(0, 0)
print(maze[n-1][m-1])