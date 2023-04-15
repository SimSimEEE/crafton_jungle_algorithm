import sys
input = sys.stdin.readline
N = int(input())
stack = [int(input()) for _ in range(N-1)]

flag = int(input())
count = 1

while stack:
    tmp = stack.pop()
    if flag < tmp:
        flag = tmp
        count+=1
        
print(count)