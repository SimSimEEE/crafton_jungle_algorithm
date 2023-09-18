def solution(a, b):
    answer = 0
    flag = a % 2 + b % 2
    if flag == 2:
        answer = a*a + b*b
    elif flag == 1:
        answer = 2*(a+b)
    else:
        answer = abs(a-b)
    return answer