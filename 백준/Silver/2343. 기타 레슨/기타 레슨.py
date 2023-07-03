n, m = map(int, input().split())
video = list(map(int, input().split()))

high = sum(video)
low = 0
mid = high
answer = high
while high >= low :
    mid = (high + low) // 2
    sum = 0
    cnt = 0
    if mid < max(video):
        low = mid+1
        continue
    for v in video:
        sum += v
        if sum  > mid:
            cnt += 1
            sum = v
    if cnt < m:
        high  = mid - 1
        answer = min(answer, mid)
    else:
        low = mid + 1

print(answer)