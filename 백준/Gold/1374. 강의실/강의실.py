import heapq
import sys

n = int(sys.stdin.readline())

lecture = []
end_heap = []
cnt = 0
room = [0] * (n+1)
for _ in range(n):
    num, start, end = map(int,input().split())
    heapq.heappush(lecture, [start,end,num])

start, end, num = heapq.heappop(lecture)
heapq.heappush(end_heap, end)
while lecture:
    start, end, num = heapq.heappop(lecture)
    if end_heap[0] <= start:
        heapq.heappop(end_heap)
    heapq.heappush(end_heap, end)

print(len(end_heap))