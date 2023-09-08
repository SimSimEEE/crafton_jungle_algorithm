def solution(my_strings, parts):
    answer = ''
    for index, [i, j] in enumerate(parts):
        answer += my_strings[index][i:j + 1]
    return answer