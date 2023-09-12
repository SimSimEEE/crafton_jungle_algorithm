from itertools import product

def solution(user_id, banned_id):
    answer = 0
    banned_idArr = [[] for _ in range(len(banned_id))]
    
    for i, bid in enumerate(banned_id):
        for uid in user_id:
            correct = True
            if len(uid) != len(bid):
                correct = False
            else:
                for idx, _ in enumerate(bid):
                    if bid[idx] != '*':
                        if bid[idx] != uid[idx]:
                            correct = False
                            break
                if correct:
                    banned_idArr[i].append(uid)
                    
    unique_combinations = set()
    
    for combination in product(*banned_idArr):
        if len(set(combination)) == len(combination):
            unique_combinations.add(tuple(sorted(combination)))
            
    return len(unique_combinations)