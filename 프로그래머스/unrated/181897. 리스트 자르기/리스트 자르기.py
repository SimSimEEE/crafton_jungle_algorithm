def solution(n, slicer, num_list):
    return num_list[slicer[0] * (n != 1) : (slicer[1] + 1) * (n != 2) + len(num_list) * (n == 2) : (n == 4) * slicer[2] + (n != 4)]