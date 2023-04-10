import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_H = max(map(max, A))
min_H = min(map(min, A))

def DFS(x,y,h):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and A[nx][ny] > h:
            visited[nx][ny] = True
            DFS(nx,ny,h)

ans = 1
for h in range(min_H,max_H):
    count = 0
    visited = [[False]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if A[x][y] > h and not visited[x][y]:
                count+=1
                visited[x][y] = True
                DFS(x,y,h)
    ans = max(ans,count)
print(ans)