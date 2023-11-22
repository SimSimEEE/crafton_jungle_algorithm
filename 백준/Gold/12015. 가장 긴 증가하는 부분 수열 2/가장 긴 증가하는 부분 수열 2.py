N = int(input())
A = list(map(int, input().split()))
dp = [A[0]]

for i in range(1, N):
    if dp[-1] < A[i]:
        dp.append(A[i])
    else:
        start, end = 0, len(dp) - 1
        while start < end:
            mid = (start + end) // 2
            if dp[mid] < A[i]:
                start = mid + 1
            else:
                end = mid
        dp[start] = A[i]

print(len(dp))