def solution(picture, k):
    answer = []
    for p in picture:
        for _ in range(k):
            answer.append(p.replace('x', 'x'*k).replace('.', '.'*k))
    return answer