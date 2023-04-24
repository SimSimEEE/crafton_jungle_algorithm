from heapq import heappush, heappop
import sys
input = sys.stdin.readline

maze = []

n = int(input())
for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

visited = [[0] * n for _ in range(n)]

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]


def dijkstra():
    q = []
    heappush(q, [0, 0, 0])
    visited[0][0] = 1

    while q:
        change_cnt, i, j = heappop(q)
        if i == n-1 and j == n-1:
            print(change_cnt)
            return
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                if maze[ni][nj] == 0:
                    heappush(q, [change_cnt + 1, ni, nj])
                else:
                    heappush(q, [change_cnt, ni, nj])

dijkstra()