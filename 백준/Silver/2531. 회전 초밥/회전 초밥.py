n, d, k, c = map(int, input().split())
conveyor = [int(input()) for _ in range(n)]
sushis = [sushi for sushi in conveyor[n-k:]]
max_sushi = 0
for i in range(n):
    cnt = len(set(sushis))
    if not c in sushis:
        cnt += 1
    max_sushi = max(max_sushi, cnt)
    sushis.append(conveyor[i])
    sushis.pop(0)
print(max_sushi)
