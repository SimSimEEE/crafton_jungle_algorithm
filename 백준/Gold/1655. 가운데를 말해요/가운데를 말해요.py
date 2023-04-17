import heapq
import sys

N = int(sys.stdin.readline())

leftHeap = []
rightHeap = []
for i in range(N):
    n = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -n)
    else:
        heapq.heappush(rightHeap, n)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        right = heapq.heappop(rightHeap)
        left = heapq.heappop(leftHeap)

        heapq.heappush(leftHeap, -right)
        heapq.heappush(rightHeap, -left)

    print(-leftHeap[0])