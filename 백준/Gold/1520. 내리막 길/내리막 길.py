import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

M,N = map(int, input().split())
graph = list(list(map(int,input().split())) for _ in range(M))
visited = list([-1]*N for _ in range(M))

drow = [1,-1,0,0]
dcol = [0,0,1,-1]

def dfs(row,col):
    if row == M-1 and col == N-1:
        return 1
    
    if visited[row][col] != -1:
        return visited[row][col]
    
    cnt = 0
    for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        if 0 <= nrow < M and 0 <= ncol < N and graph[row][col] > graph[nrow][ncol]:
            cnt += dfs(nrow,ncol)
    visited[row][col] = cnt
    return visited[row][col]
print(dfs(0,0))