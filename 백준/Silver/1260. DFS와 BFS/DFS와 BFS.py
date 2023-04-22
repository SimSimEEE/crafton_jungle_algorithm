import sys
input = sys.stdin.readline

flag = 0

def DFS(V):
    global flag
    flag = flag | 1 << V
    print(V, end=" ")
    for i in tree[V]:
        if flag & 1 << i == 0:
            DFS(i)


def BFS(V):
    flag = 0
    flag = flag | 1 << V
    print(V, end=" ")
    queue = [V]

    while (queue):
        for i in tree[queue.pop(0)]:
            if flag & 1 << i == 0:
                flag = flag | 1 << i
                print(i, end=" ")
                queue.append(i)

N, M, V = map(int, input().split())

tree = [[]for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)



for j in range(N+1):
    tree[j].sort()

DFS(V)
print()
BFS(V)