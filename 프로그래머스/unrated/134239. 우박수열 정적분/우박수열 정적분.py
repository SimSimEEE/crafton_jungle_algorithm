def solution(k, ranges):
    answer = []
    Collatz = [k]
    CollatzArea = []
    while Collatz[-1] > 1:
        if Collatz[-1]%2 == 0:
            Collatz.append(Collatz[-1]//2)
        else:
            Collatz.append(Collatz[-1] * 3 + 1)
        if len(Collatz) >= 2:
            CollatzArea.append((Collatz[-1] + Collatz[-2]) / 2)
    n = len(Collatz) - 1
    for [a, b] in ranges:
        if b <= 0:
            b = n + b
        if b < a:
            answer.append(-1)
        elif b == a:
            answer.append(0)
        else:
            answer.append(sum(CollatzArea[a:b]))
    return answer