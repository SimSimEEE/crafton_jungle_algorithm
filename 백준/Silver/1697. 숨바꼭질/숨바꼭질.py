from collections import deque
n, k = map(int, input().split())

q = deque([n])
visited = [0]*(10**5+1)
while q:
    x = q.popleft()
    if x == k:
        print(visited[x])
        break
    for jump in x-1, x+1, 2*x:
        if 0 <= jump <= 10**5 and visited[jump] == 0:
            visited[jump] = visited[x] + 1
            q.append(jump)