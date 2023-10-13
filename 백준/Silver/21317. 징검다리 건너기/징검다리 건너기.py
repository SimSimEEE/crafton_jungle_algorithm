n = int(input())
energies = []
for _ in range(n - 1):
    small_jump, big_jump = map(int, input().split())
    energies.append((small_jump, big_jump))
k = int(input())
if n == 1:
    print(0)
elif n == 2:
    print(energies[0][0])
else:
    answer = float('inf')
    for j in range(n - 2):
        dp = [float('inf')] * (n + 1)
        dp[1] = 0

        for i in range(1, n + 1):
            if i + 1 <= n:
                dp[i + 1] = min(dp[i + 1], dp[i] + energies[i - 1][0])
            if i + 2 <= n:
                dp[i + 2] = min(dp[i + 2], dp[i] + energies[i - 1][1])
            if i == j:
                dp[i + 3] = min(dp[i + 3], dp[i] + k)
        answer = min(answer, dp[n])
        
    print(answer)
