def solution(num_list):
    answer = 1
    length = len(num_list)
    if length >= 11:
        return sum(num_list)
    else:
        for num in num_list:
            answer *= num
    return answer