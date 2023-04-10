import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)
while start <= end:
    mid = (start + end) // 2
    sum_tree = sum([tree - mid for tree in trees if tree > mid])
    if sum_tree >= M:
        start = mid+1
    else:
        end = mid-1
print(end)