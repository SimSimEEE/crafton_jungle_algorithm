from collections import deque

drow = [-1, 1, 0, 0]
dcol = [0, 0, 1, -1]

def bfs():
    q = []
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                q.append([graph[i][j],0,i,j])

    q = deque(sorted(q))

    while q:
        virus, time, row, col = q.popleft()
        if time == terget_s:
            break
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < N and 0 <= ncol < N:
                if graph[nrow][ncol] == 0:
                    q.append([virus, time+1, nrow, ncol])
                    graph[nrow][ncol] = graph[row][col]

N, K = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

terget_s, terget_x, terget_y = map(int,input().split())

bfs()

print(graph[terget_x-1][terget_y-1])