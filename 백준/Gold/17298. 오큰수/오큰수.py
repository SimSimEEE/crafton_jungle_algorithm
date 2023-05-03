import sys
input = sys.stdin.readline

n = int(input())
A_arr = list(map(int,input().split()))

result = [-1]*n
stack = []

for i in range(n):
    while stack and A_arr[stack[-1]] < A_arr[i]:
        result[stack.pop()] = A_arr[i]
    stack.append(i)

print(*result)