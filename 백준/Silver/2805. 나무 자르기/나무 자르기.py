import sys
N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(trees)
while end >= start:
    mid = (end + start)//2
    result = sum([tree-mid for tree in trees if tree > mid])
    if result >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)