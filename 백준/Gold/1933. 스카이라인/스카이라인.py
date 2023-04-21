from sys import stdin
import heapq

n = int(stdin.readline())

events = []
for i in range(n):
    L, H, R = map(int, stdin.readline().split())
    events.append([L, -H, R])
    events.append([R, 0, 0])

events.sort()

res = [[0, 0]]
live = [(0, float('inf'))]


for pos, negH, R in events: 
    while live[0][1] <= pos: 
        heapq.heappop(live)
    if negH:
        heapq.heappush(live, (negH, R))
         
    if res[-1][1] != -live[0][0]:
        res.append([pos, -live[0][0]])
        print(pos, -live[0][0],end=" ")