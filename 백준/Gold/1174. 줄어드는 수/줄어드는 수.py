from itertools import combinations
n = int(input())
arr = []
for i in range(1, 11):
    for j in combinations(range(9, -1, -1), i):
        arr.append(int(''.join(map(str, j))))
if n > len(arr):
    print(-1)
else:
    print(sorted(arr)[n - 1])
