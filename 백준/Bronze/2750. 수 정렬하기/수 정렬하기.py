import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
for i in range(N-1):
    for j in range(i,N):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
print(*arr,sep="\n")