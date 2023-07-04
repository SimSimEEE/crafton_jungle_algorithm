n = int(input())
k = int(input())

start = 1
end = k
result = 0
while start < end:
    mid = (end + start) // 2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i,n)
    if k <= cnt:
        end = mid
    else:
        start = mid + 1
    
print(start)