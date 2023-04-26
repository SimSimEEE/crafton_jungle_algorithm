import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
grape = [[]for _ in range(n+1)]
indegrees = [0]*(n+1)

for _ in range(m):
    b, a, w = map(int, input().split())
    grape[a].append((b,w))
    indegrees[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [[0]*(n+1) for _ in range(n+1)]    
    q = deque()
    for i in range(1,n+1):
        if not indegrees[i]:
            q.append(i)
            for nodes in grape[i]:
                result[nodes[0]][i] = nodes[1]
    while q:
        now = q.popleft()
        for i in grape[now]:
            indegrees[i[0]]-=1
            if indegrees[i[0]] == 0:
                q.append(i[0])
            for j in range(1, n+1):
                result[i[0]][j] += result[now][j] * i[1]
    
    return result

result = topology_sort()

for i in range(1,n+1):
    if result[n][i] != 0:
        print(i, result[n][i])