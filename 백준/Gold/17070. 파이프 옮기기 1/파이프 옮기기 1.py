import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

drow = [0, 1, 1]
dcol = [1, 0, 1]

def dfs(row, col, dir):
    global cnt

    if row == N-1 and col == N-1:
        cnt += 1
        return
    if (dir == 0 or dir == 1) and col + 1 < N and graph[row][col + 1] == 0:
        dfs(row, col + 1, 0)
    if (dir == 1 or dir == 2) and row + 1 < N and graph[row + 1][col] == 0:
        dfs(row + 1, col, 2)
    if row < N-1 and col < N-1 and graph[row+1][col] == 0 and graph[row][col + 1] == 0 and graph[row+1][col+1] == 0:
        dfs(row + 1, col + 1, 1)
        
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1, 0)
print(cnt)