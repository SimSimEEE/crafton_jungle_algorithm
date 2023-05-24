import sys
from collections import deque
input = sys.stdin.readline
N, Q = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    a, b, usado = map(int, input().split())
    graph[a].append([b, usado])
    graph[b].append([a, usado])

for _ in range(Q):
    k, v = map(int, input().split())
    visited = [False]*(N+1)
    visited[v] = True
    cnt = 0
    q = deque([(v, float('INF'))])
    while q:
        v, usado = q.pop()
        for n_v, n_usado in graph[v]:
            n_usado = min(usado, n_usado)
            if n_usado >= k and not visited[n_v]:
                cnt += 1
                q.append([n_v,n_usado])
                visited[n_v] = True
    print(cnt)