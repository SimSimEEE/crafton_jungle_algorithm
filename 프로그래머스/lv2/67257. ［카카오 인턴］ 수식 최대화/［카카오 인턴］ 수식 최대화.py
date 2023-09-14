import re
from itertools import permutations

def solution(expression):
    answer = 0
    operators = ["*", "-", "+"]
    codestr = "".join(op for op in operators if op in expression)
    
    ex = re.split('[^0-9]', expression)
    order = list(filter(None, re.split('[0-9]', expression)))
            
    for code_order in permutations(codestr):
        result = evaluate_expression(ex.copy(), order.copy(), code_order)
        answer = max(answer, abs(result))
    return answer

def evaluate_expression(ex, order, code_order):
    for c in code_order:
        while c in order:
            idx = order.index(c)
            if c == "+":
                ex[idx] = int(ex[idx]) + int(ex[idx + 1])
            elif c == "-":
                ex[idx] = int(ex[idx]) - int(ex[idx + 1])
            elif c == "*":
                ex[idx] = int(ex[idx]) * int(ex[idx + 1])
            ex.pop(idx + 1)
            order.remove(c)
    return ex[0]