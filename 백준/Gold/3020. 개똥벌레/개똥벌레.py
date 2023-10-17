n, h = map(int, input().split())
obstacle = list(int(input()) for _ in range(n))

up, down = [0] * (h + 1), [0] * (h + 1)

for i in range(n):
    if i % 2:
        down[obstacle[i]] += 1
    else:
        up[obstacle[i]] += 1

for i in range(h - 1, 0, -1):
    up[i] += up[i + 1]
    down[i] += down[i + 1]

min_obstacle = n
cnt = 0

for i in range(1, h + 1):
    if min_obstacle > up[i] + down[h - i + 1]:
        min_obstacle = up[i] + down[h - i + 1]
        cnt = 1
    elif min_obstacle == up[i] + down[h - i + 1]:
        cnt += 1

print(min_obstacle, cnt)
