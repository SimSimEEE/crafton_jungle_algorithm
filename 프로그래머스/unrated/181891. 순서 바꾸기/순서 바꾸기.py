def solution(num_list, n):
    return num_list[n:] + num_list[:n-1] + [num_list[n-1]]
