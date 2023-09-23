def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        querieArr = [a for a in arr[s: e+1] if k < a]
        answer.append(min(querieArr) if querieArr else -1)
    return answer