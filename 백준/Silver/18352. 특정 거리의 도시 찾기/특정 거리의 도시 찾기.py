from collections import deque

n, m, k, x = map(int, input().split())

city = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

result = []
visited = [False] * (n + 1)
visited[x] = True
distance = [0] * (n + 1)
queue = deque([x])

while queue:
    now = queue.popleft()
    for i in city[now]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)
            distance[i] = distance[now] + 1
            if distance[i] == k:
                result.append(i)

if not result:
    print(-1)
else:
    print(*sorted(result), sep='\n')
