from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
input = stdin.readline
n, m = map(int, input().split())
height = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    if height[a - 1] > height[b - 1]:
        graph[b].append(a)
    else:
        graph[a].append(b)
def dfs(x):
    if dp[x] != 0:
        return dp[x]
    dp[x] = 1
    for nx in graph[x]:
        dp[x] = max(dp[x], dfs(nx) + 1)
    return dp[x]

for i in range(1, n + 1):
    dfs(i)
    print(dp[i])