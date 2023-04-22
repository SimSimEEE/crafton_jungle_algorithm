import sys
input = sys.stdin.readline

def DFS(V):
    global flag
    flag = flag | 1 << V
    for i in tree[V]:
        if flag & 1 << i == 0:
            DFS(i)

flag = 0

N, M = map(int, input().split())

tree = [[]for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for j in range(N+1):
    tree[j].sort()

count = 0
for i in range(1,N+1):
    if flag & 1 << i == 0:
        DFS(i)
        count+=1

print(count)