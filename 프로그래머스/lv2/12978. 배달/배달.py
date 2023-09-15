import heapq

def solution(N, road, K):
    answer = 0
    graph = {}
    for [start, end, dist] in road:
        if start in graph:
            graph[start].append([end, dist])
        else:
            graph[start] = [[end, dist]]
        if end in graph:
            graph[end].append([start, dist])
        else:
            graph[end] = [[start, dist]]
    distances = {node: float('inf') for node in graph}
    start = 1
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if distances[current_destination] < current_distance:
            continue
        for new_destination, new_distance in graph[current_destination]:
            distance = new_distance + current_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
                
    for _, key in distances.items():
        if key <= K:
            answer+=1
    return answer