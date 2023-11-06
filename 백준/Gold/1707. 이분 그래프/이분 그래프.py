import sys
sys.setrecursionlimit(10**6)

def is_bipartite(V, tree, visited, color):
    visited[V] = color
    for neighbor in tree[V]:
        if visited[neighbor] == 0:
            if not is_bipartite(neighbor, tree, visited, -color):
                return False
        elif visited[neighbor] == color:
            return False
    return True

def check_bipartite_graph(test_cases):
    for _ in range(test_cases):
        V, E = map(int, input().split())
        tree = [[] for _ in range(V + 1)]
        visited = [0] * (V + 1)
        for _ in range(E):
            u, v = map(int, input().split())
            tree[u].append(v)
            tree[v].append(u)
        flag = 0
        for i in range(V + 1):
            if visited[i] == 0:
                if not is_bipartite(i, tree, visited, 1):
                    print("NO")
                    break
        else:
            print("YES")

if __name__ == "__main__":
    input = sys.stdin.readline
    test_cases = int(input())
    check_bipartite_graph(test_cases)