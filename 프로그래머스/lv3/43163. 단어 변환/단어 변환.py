from collections import deque

def is_transformable(word1, word2):
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff_count == 1
    
def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    q = deque([(begin, 0)])
    while q:
        begin, cnt = q.popleft()
        if begin == target:
            return cnt
        for i, word in enumerate(words):
            if not visited[i] and is_transformable(word, begin):
                visited[i] = True
                q.append((word, cnt+1))
    return answer