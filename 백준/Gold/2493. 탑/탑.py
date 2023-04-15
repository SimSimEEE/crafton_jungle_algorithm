import sys
input = sys.stdin.readline
N = int(input())
towers = list(map(int, input().split()))
stack = []
result = [0]*N

for i in range(N):
    while stack:
        if stack[-1][1] >= towers[i]:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i,towers[i]])

print(*result)