def solution(n, wires):
    min_diff = float('inf')
    for i in range(len(wires)):
        edges = wires[:i] + wires[i+1:]
        nodes = set()

        graph = {}
        for edge in edges:
            a, b = edge
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            nonlocal nodes
            nodes.add(node)
            for neighbor in graph[node]:
                if neighbor not in nodes:
                    dfs(neighbor)

        all_nodes = set(graph.keys())
        tree_sizes = []
        while all_nodes:
            start_node = all_nodes.pop()
            nodes.clear()
            dfs(start_node)
            tree_sizes.append(len(nodes))

        other_tree_size = n - tree_sizes[0]
        diff = abs(tree_sizes[0] - other_tree_size)
        min_diff = min(min_diff, diff)
    
    return min_diff