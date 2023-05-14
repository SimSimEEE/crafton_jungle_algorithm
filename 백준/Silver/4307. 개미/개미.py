for _ in range(int(input())):
    l, n = map(int, input().split())
    ants = list(int(input()) for _ in range(n))
    max_time, min_time = 0, 0
    for ant in ants:
        max_time = max(max_time,max(ant, l - ant))
        min_time = max(min_time, min(ant, l - ant))
    print(min_time, max_time, sep='\n')