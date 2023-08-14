import itertools

def primenumber(x):
    for i in range(2, x):	
    	if x % i == 0:		
        	return False
    return True			

def solution(nums):
    answer = 0
    nCr = list(itertools.combinations(nums, 3))
    for C in nCr:
        if(primenumber(sum(list(C)))):
            answer+=1

    return answer

