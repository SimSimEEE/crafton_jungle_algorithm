import sys
input = sys.stdin.readline

def dfs(start, flag, tree_map, opposite):
    cnt = 1
    stack = [start]
    flag = flag | 1 << start
    while stack:
        curr = stack.pop()
        for next in tree_map[curr]:
            if flag & 1 << next == 0:
                opposite[next] += 1
                flag = flag | 1 << next
                cnt += 1
                stack.append(next)
    return cnt

N, M = map(int, input().split())

heaviness = [[]for _ in range(N+1)]
lightness = [1]*(N+1)

for i in range(M):
    a, b = map(int, input().split())
    heaviness[a].append(b)

result = 0
flag = 0
for i in range(1, N+1):
    if flag & 1 << i == 0:
        if dfs(i, flag, heaviness, lightness) > (N+1)//2:
            result += 1

for i in range(1,N+1):
    if lightness[i] > (N+1)//2:
        result += 1

print(result)