n = int(input())
start, end = 0, 1
result = 1
sum_num = 1
while end < n:
    if sum_num < n:
        end += 1
        sum_num += end
    elif sum_num >= n:
        sum_num -= start
        start += 1
        if sum_num == n:
            result += 1
print(result)