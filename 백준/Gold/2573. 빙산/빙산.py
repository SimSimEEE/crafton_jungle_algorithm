import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

def melt(x, y):
    cnt = 0 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                cnt += 1

    if cnt != 0:
        return x, y, cnt
    else:
        return None

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and arr[nx][ny] != 0:
                dfs(nx, ny)

N, M = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0

while True:
    answer += 1

    reduce = []
    for x in range(1, N):
        for y in range(1, M):
            if arr[x][y] != 0:
                h = melt(x, y)

                if h is not None:
                    reduce.append(h)

    for x, y, h in reduce:
        arr[x][y] = arr[x][y] - h if arr[x][y] - h > 0 else 0

    cnt = 0
    visited = [[False] * M for _ in range(N)]

    for x in range(1, N):
        for y in range(1, M):
            if arr[x][y] != 0 and not visited[x][y]:
                cnt += 1

                if cnt == 2:
                    break

                dfs(x, y)

    if cnt > 1: 
        break

    if sum(map(sum, arr[1:-1])) == 0:
        answer = 0
        break

print(answer)