def solution(arr):
    ln = len(arr)
    s = ln
    e = 0
    for i in range(ln):
        if arr[i] == 2:
            s = min(s, i)
            e = max(e, i)
    return arr[s:e+1] if s != ln else [-1]