def solution(strArr):
    tmp = [0] * 31
    for e in strArr:
        tmp[len(e)] += 1
    return max(tmp)