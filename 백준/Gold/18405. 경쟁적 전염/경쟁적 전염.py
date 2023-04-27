from collections import deque

drow = [-1, 1, 0, 0]
dcol = [0, 0, 1, -1]

def bfs():
    while q:
        time, row, col = q.popleft()
        if time == terget_s:
            break
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < N and 0 <= ncol < N:
                if grape[nrow][ncol] == 0:
                    q.append([time+1, nrow, ncol])
                    grape[nrow][ncol] = grape[row][col]

N, K = map(int,input().split())

grape = [list(map(int,input().split())) for _ in range(N)]

terget_s, terget_x, terget_y = map(int,input().split())

q = deque([])
for k in range(1,K+1):
    for i in range(N):
        for j in range(N):
            if grape[i][j] == k:
                q.append([0,i,j])

bfs()

print(grape[terget_x-1][terget_y-1])