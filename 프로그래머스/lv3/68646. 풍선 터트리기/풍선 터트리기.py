def solution(a):
    answer = 0
    left_min, right_min = float("inf"), float("inf")
    min_value = min(a)
    
    # 왼쪽에서 최솟값 찾기
    for i in range(len(a)):
        if a[i] == min_value:
            break
        if a[i] < left_min:
            left_min = a[i]
            answer += 1
    
    # 오른쪽에서 최솟값 찾기
    for i in range(len(a) - 1, -1, -1):
        if a[i] == min_value:
            break
        if a[i] < right_min:
            right_min = a[i]
            answer += 1
    
    return answer + 1
