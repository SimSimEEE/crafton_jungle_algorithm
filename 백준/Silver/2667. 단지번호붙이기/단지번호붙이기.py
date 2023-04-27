from collections import deque

drow = [-1, 1, 0, 0]
dcol = [0, 0, 1, -1]

def bfs(row, col, cnt):
    q = deque([[row, col]])
    visited[row][col] = True
    while q:
        row, col = q.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < N and 0 <= ncol < N and grape[nrow][ncol] == 1 and visited[nrow][ncol] == False:
                q.append([nrow, ncol])
                visited[nrow][ncol] = True
                cnt += 1
    return cnt

    

N = int(input())

grape = [list(map(int,input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        cnt = 1
        if not visited[i][j] and grape[i][j] == 1:
            result.append(bfs(i,j,cnt))

print(len(result),*sorted(result),sep="\n")