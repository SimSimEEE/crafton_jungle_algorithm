import heapq

n, m = map(int,input().split())
INF = float("INF")

graph = [[] for _ in range(n+1)] 

distance = [INF] * (n+1)

start = int(input())

for _ in range(m):
    u, v, w = map(int, input().split())  
    graph[u].append((v, w))            

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) 

        if distance[now] < dist:  
            continue               

        for i in graph[now]:     
            if dist+i[1] < distance[i[0]]:  
                distance[i[0]] = dist+i[1]   
                heapq.heappush(q, (dist+i[1], i[0]))

dijkstra(start)
for d in distance[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)
