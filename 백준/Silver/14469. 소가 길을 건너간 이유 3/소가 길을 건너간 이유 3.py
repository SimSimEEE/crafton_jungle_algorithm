cows = list(list(map(int,input().split()))for _ in range(int(input())))
cows.sort()
current_time = 0 
for arrival_time, duration_time in cows:
    current_time = max(current_time,arrival_time) + duration_time
print(current_time)