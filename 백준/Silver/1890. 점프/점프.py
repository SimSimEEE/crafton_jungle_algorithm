import sys
input = sys.stdin.readline
n = int(input())
board = list(list(map(int,input().split())) for _ in range(n))
dp = list([0]*n for _ in range(n))
dp[0][0] = 1

for row in range(n):
    for col in range(n):
        if row == n-1 and col == n-1:
            print(dp[row][col])
        d = board[row][col]
        nrow = row + d
        ncol = col + d
        
        if nrow < n:
            dp[nrow][col] += dp[row][col]
        if ncol < n:
            dp[row][ncol] += dp[row][col]