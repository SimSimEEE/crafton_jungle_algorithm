for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    dp = [0] * (money + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i], money + 1):
            dp[j] += dp[j - coins[i]]
    print(dp[money])
