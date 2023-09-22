def solution(l, r):
    answer = []
    num = [1, 2, 3, 4, 6, 7, 8, 9]
    for i in range(l, r + 1):  
        if not (str(i).replace("5","")).replace("0",""): 
            answer.append(i)
    return answer if answer else [-1]