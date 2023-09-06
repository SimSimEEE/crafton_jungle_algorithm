def solution(order):
    expected = 1 
    index = 0 
    stack = []
    
    for num in order:
        while expected <= num:
            stack.append(expected);
            expected += 1
            
        if stack[-1] == num:
            stack.pop()
            index+=1
        else:
            return index
    return index
