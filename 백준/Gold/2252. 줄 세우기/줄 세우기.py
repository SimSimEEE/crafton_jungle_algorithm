import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grape = [[]for _ in range(n+1)]
indegrees = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    grape[a].append(b)
    indegrees[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()
    for i in range(1,n+1):
        if not indegrees[i]:
            q.append(i)

    while q:
        now = q.popleft()
        for i in grape[now]:
            indegrees[i]-=1
            if indegrees[i] == 0:
                q.append(i)
        result.append(now)
    
    return result

print(*topology_sort())