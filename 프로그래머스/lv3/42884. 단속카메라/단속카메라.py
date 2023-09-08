def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1]))
    camera_position = -30001
    for route in routes:
        start, end = route
        if start > camera_position:
            camera_position = end
            answer += 1

    return answer
