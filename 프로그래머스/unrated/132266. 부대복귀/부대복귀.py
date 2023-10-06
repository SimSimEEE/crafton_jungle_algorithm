def solution(n, roads, sources, destination):
    graph = {}
    for s, e in roads:
        graph.setdefault(s, []).append(e)
        graph.setdefault(e, []).append(s)

    def bfs(destination, visited):
        queue = [(destination, 0)]
        visited[destination] = 0
        
        while queue:
            node, cnt = queue.pop(0)
            for path in graph.get(node, []):
                if visited[path] is False:
                    visited[path] = cnt + 1
                    queue.append((path, cnt + 1))

    visited = [False] * (n + 1)
    bfs(destination, visited)
    
    answer = []
    for source in sources:
        shortest_path = visited[source]
        if shortest_path is False:
            shortest_path = -1
        answer.append(shortest_path)
    return answer