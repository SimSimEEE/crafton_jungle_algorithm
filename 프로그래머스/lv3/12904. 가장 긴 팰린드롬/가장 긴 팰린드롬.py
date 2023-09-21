def solution(s):
    n = len(s)
    if n <= 1:
        return n

    dp = [[False] * n for _ in range(n)]

    max_len = 1  

    for i in range(n):
        dp[i][i] = True

    start = 0 

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2
            start = i

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    max_len = length
                    start = i

    return len(s[start:start + max_len])