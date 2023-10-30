from itertools import combinations
list_p = []
sum_p = 0
for _ in range(9):
    list_p.append(int(input()))
    sum_p += list_p[-1]
list_p.sort()
for i in combinations(list_p, 7):
    if sum(i) == 100:
        for j in i:
            print(j)
        break