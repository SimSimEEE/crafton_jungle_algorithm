dx = [1,-1]
dy = [1,-1]

def DFS(x,y,ridge,visited):
    visited[x][y] = True
    if ridge == '|':
        for i in range(2):
            nx = x + dx[i]
            if 0<=nx<N:
                if not visited[nx][y] and grape[nx][y] == ridge:
                    DFS(nx,y,ridge,visited)
    else:
        for i in range(2):
            ny = y + dy[i]
            if 0<=ny<M:
                if not visited[x][ny] and grape[x][ny] == ridge:
                    DFS(x,ny,ridge,visited)

N, M = map(int,input().split())

grape = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            DFS(i,j,grape[i][j],visited)
            cnt += 1

print(cnt)