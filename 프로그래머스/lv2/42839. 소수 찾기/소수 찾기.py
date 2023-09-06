import itertools

def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num = list(numbers)
    numList = []
    
    for r in range(1, len(num) + 1):
        for nCr in list(itertools.permutations(num, r)):
            numList.append(int(''.join(str(s) for s in nCr)))
    
    numList = set(numList)
    for n in numList:
        if is_prime_number(n):
            answer += 1
    return answer
