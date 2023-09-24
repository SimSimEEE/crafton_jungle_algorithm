from datetime import datetime

def solution(date1, date2):
    dt1 = datetime(date1[0], date1[1], date1[2])
    dt2 = datetime(date2[0], date2[1], date2[2])
    return int(dt1 < dt2)