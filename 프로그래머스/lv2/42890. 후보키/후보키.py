from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    answer = []
    for n in range(1, col+1):
        nCr = combinations(range(col), n)
        for i in nCr:
            tmp = [tuple([item[key] for key in i]) for item in relation]
            if len(set(tmp)) == row:
                for a in answer:
                    if set(a).issubset(i):
                        break
                else:
                    answer.append(i)
    return len(answer)