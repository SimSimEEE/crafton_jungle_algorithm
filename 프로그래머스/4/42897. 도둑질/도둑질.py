def solution(money):
    answer = 0
    ln = len(money)
    dp1 = [0] + money[:ln-1]
    dp2 = [0] + money[1:]
    for i in range(ln):
        if i > 1:
            dp1[i] = max(dp1[i - 1], dp1[i] + dp1[i - 2])
            dp2[i] = max(dp2[i - 1], dp2[i] + dp2[i - 2])
    return max(dp1[-1], dp2[-1])