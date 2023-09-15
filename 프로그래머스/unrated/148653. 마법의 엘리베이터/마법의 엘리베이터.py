def solution(storey):
    answer = 0
    while storey > 0:
        tmp = storey % 10
        storey //= 10
        if tmp > 5:
            storey += 1
            tmp = 10 - tmp
        elif tmp == 5:
            if storey%10 >= 5:
                storey+=1
        answer += tmp
    return answer