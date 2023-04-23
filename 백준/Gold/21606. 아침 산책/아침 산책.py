import sys
input = sys.stdin.readline


def DFS(V, cnt):
    global flag
    flag = flag | 1 << V
    for i in tree[V]:
        if flag & 1 << i == 0:
            if side[i-1] == '1':
                cnt += 1
            else :
                cnt = DFS(i, cnt)

    return cnt


V = int(input())
side = input().rstrip()
tree = [[]for _ in range(V+1)]
result = 0

for _ in range(V-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
    if side[u-1] == '1' and side[v-1] == '1':
        result += 2

flag = 0
for i in range(1, V+1):
    if side[i-1] == '0' and flag & 1 << i == 0:
        tmp = DFS(i, 0)
        result = tmp*(tmp-1)
print(result)