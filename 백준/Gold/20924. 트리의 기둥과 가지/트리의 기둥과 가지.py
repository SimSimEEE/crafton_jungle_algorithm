from collections import deque
n, r = map(int, input().split())
maps = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, d = map(int, input().split())
    maps[a].append((b, d))
    maps[b].append((a, d))


def bfs(start):
    q = deque()
    q.append(start)
    visit = [0] * (n + 1)
    visit[start] = 1
    max_dist = 0
    root = 0
    if len(maps[start]) == 1:
        is_root = True
    else:
        is_root = False
    while q:
        now = q.popleft()
        for nxt, dist in maps[now]:
            if not visit[nxt]:
                visit[nxt] = visit[now] + dist
                max_dist = max(max_dist, visit[nxt])
                q.append(nxt)
                if len(maps[nxt]) != 2 and is_root:
                    is_root = False
                    root = visit[nxt] - 1
    return root, max_dist - 1 - root


if n == 1:
    print(0, 0)
else:
    print(*bfs(r))
