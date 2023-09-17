def solution(jobs):
    answer = 0
    current_time = 0
    total_job = len(jobs)
    jobs.sort(key=lambda x: (x[1], x[0])) 

    while jobs:
        for job in jobs:
            if job[0] <= current_time:
                current_time += job[1] 
                answer += current_time - job[0]
                jobs.remove(job)
                break
        else:
            current_time += 1 

    return answer // total_job