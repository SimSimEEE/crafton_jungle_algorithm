def solution(genres, plays):
    answer = []
    maps = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in maps:
            maps[genre] = [(i, play)]
        else:
            maps[genre].append((i, play))
            
    for genre in maps:
        maps[genre].sort(key=lambda x: (-x[1], x[0]))
    
    for genre in sorted(maps, key=lambda x: sum(play for _, play in maps[x]), reverse=True):
        for i, _ in maps[genre][:2]:
            answer.append(i)

    return answer
