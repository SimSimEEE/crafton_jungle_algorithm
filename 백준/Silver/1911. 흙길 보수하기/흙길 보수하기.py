import sys
import math

input = sys.stdin.readline
N, L = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(N))
graph.sort(key=lambda x: x[0], reverse=True)
cnt = 0
board = 0
while graph:
    start, end = graph.pop()
    if start > end:
        continue
    if board > start:
        start = board
    if start < end:
        n = math.ceil((end - start) / L)
        start += L * n
        cnt += n
    board = start

print(cnt)