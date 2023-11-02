def determinant(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1
coordination = []
for _ in range(int(input())):
    coordination.append(list(map(int, input().split())))
result = 0
for i in range(len(coordination)):
    result += determinant(coordination[i - 1][0], coordination[i - 1][1], coordination[i][0], coordination[i][1])
print(abs(round(result / 2, 1)))
