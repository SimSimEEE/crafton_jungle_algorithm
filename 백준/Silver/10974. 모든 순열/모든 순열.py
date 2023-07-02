from itertools import permutations
n = int(input())
nCn = list(permutations(range(1, n+1),n))

for c in nCn:
    print(*c)