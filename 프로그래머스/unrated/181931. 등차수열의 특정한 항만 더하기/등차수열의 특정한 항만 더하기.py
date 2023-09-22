def solution(a, d, included):
    return sum([a + d * i for i, bo in enumerate(included) if bo])