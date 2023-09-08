import math

def solution(n, stations, w):
    answer = 0
    start = 1
    
    for station in stations:
        left_range = station - w
        right_range = station + w
        
        if left_range > start:
            answer += math.ceil((left_range - start) / (2 * w + 1))
        
        start = right_range + 1
    
    if start <= n:
        answer += math.ceil((n - start + 1) / (2 * w + 1))
    
    return answer
