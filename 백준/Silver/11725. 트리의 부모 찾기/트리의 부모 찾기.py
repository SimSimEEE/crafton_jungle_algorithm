import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(V,root):
    global flag
    flag = flag | 1 << V
    for i in tree[V]:
        if flag & 1 << i == 0:
            root[i] = V
            DFS(i,root)

flag = 0

N = int(input())

tree = [[]for _ in range(N+1)]
root = [0]*(N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for j in range(N+1):
    tree[j].sort()

DFS(1,root)

print(*root[2:],sep="\n")