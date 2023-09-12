def solution(gems):
    gem_count = len(set(gems))
    
    if len(gems) == gem_count:
        return [1, gem_count]
    
    gem_freq = {}
    left, right = 0, 0
    answer = []
    
    for right in range(len(gems)):
        if gems[right] not in gem_freq:
            gem_freq[gems[right]] = 1
        else:
            gem_freq[gems[right]] += 1
        
        while len(gem_freq) == gem_count:
            if not answer or (right - left) < (answer[1] - answer[0]):
                answer = [left + 1, right + 1]
            
            gem_freq[gems[left]] -= 1
            if gem_freq[gems[left]] == 0:
                del gem_freq[gems[left]]
            
            left += 1
    
    return answer
