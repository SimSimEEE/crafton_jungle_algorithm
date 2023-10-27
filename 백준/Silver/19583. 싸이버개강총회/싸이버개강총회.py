import sys
input = sys.stdin.readline

def time_to_min(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

s, e, q = map(time_to_min, input().split())
streaming = {}
answer = 0

while True:
    try:
        t, n = input().split()
        t = time_to_min(t)
    except:
        break

    if n not in streaming:
        if t <= s:
            streaming[n] = 1
    elif e <= t <= q:
        del streaming[n]
        answer += 1

print(answer)