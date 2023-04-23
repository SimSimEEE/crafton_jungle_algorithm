import sys
input = sys.stdin.readline

def DFS(V,start):
    global flag, result
    flag[start] = flag[start] | 1 << V
    flag[V] = flag[V] | 1 << start
    for i in tree[V]:
        if flag[start] & 1 << i == 0:
            if side[i-1] == '0':
                DFS(i,start)
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
flag = [0]*(V+1)
for i in range(1, V+1):
    if side[i-1] == '1':
        DFS(i,i)

print(result)