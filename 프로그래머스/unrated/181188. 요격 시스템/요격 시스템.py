def solution(targets):
    answer = 0
    targets.sort(key = lambda x : x[1])
    flag = 0
    for s,e in targets:
        if s >= flag:
            answer += 1
            flag = e
    return answer