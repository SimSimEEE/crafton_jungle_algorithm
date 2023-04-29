import sys
input = sys.stdin.readline

INF = float("INF")

N = int(input())
city_graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(1 << (N-1)) for _ in range(N)]

def TSP(current_city, visited):
    if dp[current_city][visited] != 0:
        return dp[current_city][visited]
    
    if visited == (1 << (N-1))-1:
        if city_graph[current_city][0]:
            return city_graph[current_city][0]
        else:
            return INF

    min_distance = INF
    for next_city in range(1, N):
        if not city_graph[current_city][next_city]:
            continue
        if visited & (1 << next_city - 1):
            continue
        distance = TSP(next_city, visited | 1 << (next_city-1)) + city_graph[current_city][next_city]
        if min_distance > distance:
            min_distance = distance
    dp[current_city][visited] = min_distance
    return min_distance

print(TSP(0, 0))