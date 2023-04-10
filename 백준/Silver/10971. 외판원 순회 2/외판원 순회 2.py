import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
m = sys.maxsize
sum = 0
arr = [0]*N


def TSP(cnt, flag, sum):
    global m
    if cnt == N:
        if W[arr[-1]][0] != 0:
            m = min(m, sum + W[arr[-1]][0])
        sum = 0
        return
    else:
        for i in range(1, N):
            if flag & 1 << i != 0 or W[arr[cnt-1]][i] == 0:
                continue
            arr[cnt] = i
            TSP(cnt+1, flag | 1 << i, sum + W[arr[cnt-1]][i])


TSP(1, 0, 0)
print(m)