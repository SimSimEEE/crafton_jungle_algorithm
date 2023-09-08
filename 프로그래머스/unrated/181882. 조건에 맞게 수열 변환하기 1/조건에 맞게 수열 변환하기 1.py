def solution(arr):
    for i, a in enumerate(arr):
        if a >= 50 and a%2 == 0:
            arr[i] //= 2
        elif a < 50 and a%2 == 1:
            arr[i] *= 2
    return arr