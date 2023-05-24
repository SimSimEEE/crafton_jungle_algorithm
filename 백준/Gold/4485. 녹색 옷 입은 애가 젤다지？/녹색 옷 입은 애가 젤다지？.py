import sys
from collections import deque
input = sys.stdin.readline

drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

problem_num = 0
while True:
    N = int(input())
    if N == 0:
        break
    visited = [[float('inf')]*N for _ in range(N)]
    graph = [list(map(int, input().split())) for _ in range(N)]
    q = deque([(0, 0, graph[0][0])]) 
    visited[0][0] = graph[0][0]
    while q:
        row, col, rupee = q.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < N and 0 <= ncol < N:
                min_rupee = rupee + graph[nrow][ncol]
                if min_rupee < visited[nrow][ncol]:
                    visited[nrow][ncol] = min_rupee
                    q.append((nrow, ncol, min_rupee))
    problem_num += 1
    print("Problem {}: {}".format(problem_num, visited[N-1][N-1]))