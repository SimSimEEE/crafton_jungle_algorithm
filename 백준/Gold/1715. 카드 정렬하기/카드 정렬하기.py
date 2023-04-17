import sys
import heapq
input = sys.stdin.readline

result = 0
N = []

for i in range(int(input())):
    heapq.heappush(N,int(input()))

for i in range(len(N)-1):
    shuffle = heapq.heappop(N) + heapq.heappop(N)
    heapq.heappush(N,shuffle)
    result += shuffle

print(result)