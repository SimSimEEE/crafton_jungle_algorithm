from collections import deque


def prime_list():
    n = 9999
    a = [False, False] + [True]*(n-1)

    for i in range(2, 100):
        if a[i]:
            for j in range(2*i, n+1, i):
                a[j] = False
    return a

def bfs(t1, t2):
    visited = [0] * 10000
    visited[t1] = 1
    queue = deque()
    queue.append([t1, 0])
    cnt = 0
    while queue:
        n, cnt = queue.popleft()
        if n == t2:
            return cnt
        strn = str(n)
        for i in range(4):
            for j in range(10):
                temp = int(strn[:i] + str(j) + strn[i+1:])
                if p_list[temp] and temp >= 1000 and visited[temp] == 0:
                    visited[temp] = 1
                    queue.append([temp, cnt+1])
                    
n = int(input())
p_list = prime_list()
for _ in range(n):
    start, end = map(int, input().split())
    cnt = bfs(start, end)
    print(cnt if cnt != None else "Impossible")
