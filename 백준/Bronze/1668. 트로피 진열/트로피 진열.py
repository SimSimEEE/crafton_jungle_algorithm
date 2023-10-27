n = int(input())
trophy = [int(input()) for _ in range(n)]
left = trophy[0]
right = trophy[-1]
left_cnt = 1
right_cnt = 1
for i in range(1, n):
    if left < trophy[i]:
        left = trophy[i]
        left_cnt += 1
for i in range(n - 2, -1, -1):
    if right < trophy[i]:
        right = trophy[i]
        right_cnt += 1
print(left_cnt)
print(right_cnt)