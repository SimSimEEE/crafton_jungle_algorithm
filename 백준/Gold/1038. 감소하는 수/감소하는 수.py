from itertools import combinations
n = int(input())
nums = range(9, -1, -1)
result = []
if n > 1022:
    print(-1)
    exit()
for i in range(1, 11):
    for j in combinations(nums, i):
        result.append(int("".join(map(str, j))))
    if len(result) >= n + 1:
        break
result.sort()
print(result[n])
