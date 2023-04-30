n = int(input())
meeting_schedule = list(tuple(map(int,input().split())) for _ in range(n))
meeting_schedule = sorted(meeting_schedule,key=lambda x : (x[1],x[0]))

meeting_end, meeting_count = 0, 0
for start, end in meeting_schedule:
    if start >= meeting_end:
        meeting_end = end
        meeting_count+=1
print(meeting_count)