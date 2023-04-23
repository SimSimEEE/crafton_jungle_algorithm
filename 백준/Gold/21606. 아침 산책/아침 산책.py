import sys
input = sys.stdin.readline

def DFS(V):
    global flag
    global result
    flag = flag | 1 << V
    for i in tree[V]:
        if flag & 1 << i == 0:
            if side[i-1] == '0':
                DFS(i)
            else:
                result+=1

V = int(input())
side = input().rstrip()
tree = [[]for _ in range(V+1)]

for _ in range(V-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

result = 0
for i in range(1, V+1):
    flag = 0
    if side[i-1] == '1':
        DFS(i)

print(result)