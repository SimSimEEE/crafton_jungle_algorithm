def solution(arr):
    dif = len(arr) - len(arr[0])
    if dif > 0:
        for i in range(len(arr)):
            for _ in range(dif):
                arr[i].append(0)
    elif dif < 0:
        for i in range(-dif):
            arr.append([0]*len(arr[0]))
    return arr