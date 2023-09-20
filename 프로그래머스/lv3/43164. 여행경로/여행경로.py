def dfs(maps, visited, start, answer, tickets):
    if len(answer) == len(tickets) + 1:
        return
    if start not in maps:
        return
    for i, dest in enumerate(maps[start]):
        if not visited[start][i]:
            visited[start][i] = True
            answer.append(dest)
            dfs(maps, visited, dest, answer, tickets)
            if len(answer) == len(tickets) + 1:
                return
            visited[start][i] = False
            answer.pop()

def solution(tickets):
    answer = ["ICN"]
    maps = {}

    for start, end in tickets:
        if start in maps:
            maps[start].append(end)
            maps[start].sort()
        else:
            maps[start] = [end]

    visited = {}
    for key in maps:
        visited[key] = [False] * len(maps[key])

    dfs(maps, visited, "ICN", answer, tickets)
    return answer