from collections import deque

def change_time(time):
    return int(time[:2]) * 60 + int(time[3:])

def solution(plans):
    plans = sorted(list(
        map(lambda x: [x[0], change_time(x[1]), int(x[2])], plans)), key=lambda x: x[1])
    result, waiting, current_time = [], deque([plans[0]]), plans[0][1]

    for i, task in enumerate(plans[1:]):
        next_time = task[1]

        while waiting:
            name, start_time, playtime = waiting.pop()
            if start_time > current_time:
                current_time = start_time
            end_time = current_time + playtime

            if end_time <= next_time:
                current_time += playtime
                result.append(name)
            else:
                current_time = next_time
                waiting.append([name, start_time, end_time - next_time])
                break

        waiting.append(task)

    while waiting:
        result.append(waiting.pop()[0])

    return result
