def solution(arr):
    answer = 100
    cnt = 0
    while True:
        new_arr = [i // 2 if i >= 50 and i % 2 == 0 else i * 2 + 1 if i < 50 and i % 2 == 1 else i for i in arr]
        if new_arr == arr:
            break
        arr = new_arr
        cnt += 1
    return cnt
