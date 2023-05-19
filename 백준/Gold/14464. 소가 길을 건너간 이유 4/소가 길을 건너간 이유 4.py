import heapq

C, N = map(int, input().split())
chickens = sorted(list(int(input()) for _ in range(C)))
cows = []
for _ in range(N):
    s, e = map(int, input().split())
    heapq.heappush(cows, (e, s))

cnt = 0
while cows and chickens:
    e, s = heapq.heappop(cows)
    for i in range(len(chickens)):
        if s <= chickens[i] <= e:
            cnt += 1
            chickens.pop(i)
            break

print(cnt)