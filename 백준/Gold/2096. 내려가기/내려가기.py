n = int(input())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dp_max = [[0, 0, 0] for _ in range(2)]
dp_min = [[0, 0, 0] for _ in range(2)]

for i in range(n):
    for j in range(3):
        if i == 0:
            dp_max[1][j] = dp_max[0][j] = dp_min[1][j] = dp_min[0][j] = maps[i][j]
        else:
            dp_max[1][j] = max(dp_max[0][j], dp_max[0][j-1] if j > 0 else 0, dp_max[0][j+1] if j < 2 else 0) + maps[i][j]
            dp_min[1][j] = min(dp_min[0][j], dp_min[0][j-1] if j > 0 else float('inf'), dp_min[0][j+1] if j < 2 else float('inf')) + maps[i][j]
    dp_max[0], dp_max[1] = dp_max[1], dp_max[0]
    dp_min[0], dp_min[1] = dp_min[1], dp_min[0]

max_val = max(dp_max[0])
min_val = min(dp_min[0])

print(max_val, min_val)
