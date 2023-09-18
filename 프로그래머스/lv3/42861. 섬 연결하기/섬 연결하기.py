def find_parent(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union(parent, u, v):
    u = find_parent(parent, u)
    v = find_parent(parent, v)
    if u != v:
        parent[u] = v

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    parent = {i: i for i in range(n)}
    
    for u, v, cost in costs:
        if find_parent(parent, u) != find_parent(parent, v):
            union(parent, u, v)
            answer += cost

    return answer