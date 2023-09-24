import math
def solution(arr):
    arr.extend([0] * (2 ** math.ceil(math.log2(len(arr))) - len(arr)))
    return arr