from itertools import combinations_with_replacement

def calculate_score(lion_list, info):
    lion = appach = 0
    for i, c in enumerate(lion_list):
        if c > info[i]:
            lion += 10 - i
        elif c <= info[i] and info[i] != 0:
            appach += 10 - i
    return lion, appach

def solution(n, info):
    answer = [-1]
    result = 0
    for nCr in combinations_with_replacement(range(10, -1, -1), n):
        lion_list = [0] * 11
        for i in nCr:
            lion_list[i] += 1
        
        lion, appach = calculate_score(lion_list, info)
        
        if lion > appach and result < lion - appach:
            result = lion - appach
            answer = lion_list
    
    return answer