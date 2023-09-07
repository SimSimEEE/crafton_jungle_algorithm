def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    a_idx = 0

    for b in B:
        if A[a_idx] < b:
            answer += 1
            a_idx += 1

    return answer