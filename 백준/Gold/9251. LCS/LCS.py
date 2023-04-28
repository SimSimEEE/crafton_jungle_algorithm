first_str = input()
second_str = input()

DP = [0]*(len(second_str))
for i in range(len(first_str)):
    cnt = 0
    for j in range(len(second_str)):
        if cnt < DP[j]:
            cnt = DP[j]
        elif first_str[i] == second_str[j]:
            DP[j] = cnt+1
print(max(DP))