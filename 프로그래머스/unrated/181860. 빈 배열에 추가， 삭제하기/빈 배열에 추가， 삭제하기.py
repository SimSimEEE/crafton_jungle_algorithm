def solution(arr, flag):
    answer = []
    for i, e in enumerate(flag):
        if e:
            for _ in range(arr[i] * 2):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                answer.pop()
    return answer