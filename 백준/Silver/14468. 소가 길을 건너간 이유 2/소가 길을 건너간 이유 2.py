cows = list(input())
cnt = 0

for start in range(51):
    for end in range(start+1,52):
        if cows[start] == cows[end]:
            cows_between = cows[start:end+1]
            for cow in cows_between:
                if cows_between.count(cow) == 1:
                    cnt += 1
print(cnt//2)