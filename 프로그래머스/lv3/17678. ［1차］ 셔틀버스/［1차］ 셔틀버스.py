def solution(n, t, m, timetable):
    timetable = [int(time[:2]) * 60 + int(time[-2:]) for time in timetable]
    timetable.sort()
    answer = 540 + (n-1) * t
    for i in range(n):
        current_bus = 540 + i*t
        available_passenger = m
        while timetable:
            if available_passenger > 0 and current_bus >= timetable[0]:
                passenger = timetable.pop(0)
                available_passenger -= 1
            else:
                break
    if available_passenger != 0:
        answer = 540 + (n-1) * t
    else:
        answer = passenger - 1
    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)