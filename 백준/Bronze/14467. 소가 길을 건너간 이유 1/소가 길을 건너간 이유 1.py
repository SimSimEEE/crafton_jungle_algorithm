cows = [-1]*11
cnt = 0
for _ in range(int(input())):
    for cow_num, idx  in [map(int,input().split())]:
        if cows[cow_num] == -1:
            cows[cow_num] = idx
        elif cows[cow_num] != idx:
            cnt+=1
            cows[cow_num] = idx
        else:
            cows[cow_num] = idx
print(cnt)