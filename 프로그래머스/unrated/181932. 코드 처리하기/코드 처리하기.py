def solution(code):
    answer = ''
    mode = 0
    for i, c in enumerate(code):
        if c == "1":
            mode = 1 - mode
            continue
        if mode == 0 and i % 2 == 0:
            answer += c
        elif mode == 1 and i % 2 == 1:
            answer += c
    return answer if answer else "EMPTY"