def solution(order):
    answer = 0
    for e in order:
        if "cafelatte" in e:
            answer += 5000
        else:
            answer += 4500
    return answer