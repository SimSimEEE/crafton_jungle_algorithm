cos = []
for i in range(int(input())):
    cos.append([*map(int, input().split())])
mid_x = sorted(cos, key=lambda x: (x[0]))[len(cos) // 2][0]
mid_y = sorted(cos, key=lambda x: (x[1]))[len(cos) // 2][1]
print(sum(abs(mid_x - x) + abs(mid_y - y) for x, y in cos))