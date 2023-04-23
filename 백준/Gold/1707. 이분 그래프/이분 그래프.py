import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(V,color):
    visited[V] = color
    for i in tree[V]:
        if visited[i] == 0:
            if not DFS(i,-color):
                return False
        elif visited[i] == color:
            return False
    return True

for _ in range(int(input())):
    V, E = map(int, input().split())
    tree = [[]for _ in range(V+1)]
    visited = [0]*(V+1)
    flag = 0
    for _ in range(E):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    for i in range(V+1):
        if visited[i] == 0:
            if not DFS(i,1):
                print("NO")
                break
    else:
        print("YES")