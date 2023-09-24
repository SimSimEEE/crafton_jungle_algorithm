def solution(intStrs, k, s, l):
    return [num for intStr in intStrs if (num := int(intStr[s:s+l])) > k]
