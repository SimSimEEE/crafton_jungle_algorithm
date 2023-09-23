import heapq

def dijkstra(graph, start, end):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distance[current_node]:
            continue
        
        if current_node == end:
            return distance[end]
        
        for neighbor, weight in graph[current_node].items():
            distance_to_neighbor = current_distance + weight
            
            if distance_to_neighbor < distance[neighbor]:
                distance[neighbor] = distance_to_neighbor
                heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))
    
    return float('inf')

def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = {}
    for start, end, fare in fares:
        if start in graph:
            graph[start][end] = fare
        else:
            graph[start] = {end: fare}
        if end in graph:
            graph[end][start] = fare
        else:
            graph[end] = {start: fare}
    
    for i in range(1, n + 1):
        s_to_i = dijkstra(graph, s, i)
        a_to_i = dijkstra(graph, a, i)
        b_to_i = dijkstra(graph, b, i)
        answer = min(answer, s_to_i + a_to_i + b_to_i)
    
    return answer