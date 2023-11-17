from itertools import combinations
n = int(input())
s = list(map(int, input().split()))
num_list = [0] * 2000001
for i in range(1, n + 1):
    for j in combinations(s, i):
        num_list[sum(j)] = 1

for i in range(1, 2000001):
    if num_list[i] == 0:
        print(i)
        break