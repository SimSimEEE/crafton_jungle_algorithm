function solution(n, edge) {
    var answer = 0;
    let graph = new Map();
    let visited = new Array(n + 1);
    visited.fill(0);
    
    for (let i = 1; i <= n; i++) {
        graph.set(i, []);
    }

    edge.forEach(([fromEdge, toEdge]) => {
        graph.get(fromEdge).push(toEdge);
        graph.get(toEdge).push(fromEdge);
    });
    
    let queue = [1];
    visited[1] = 1;

    while (queue.length > 0) {
        let node = queue.shift();
        graph.get(node).forEach((adjNode) => {
            if (visited[adjNode] === 0) {
                queue.push(adjNode);
                visited[adjNode] = visited[node] + 1;
            }
        });
    }
    
    let maxDistance = Math.max(...visited);
    for (let i = 1; i <= n; i++) {
        if (visited[i] === maxDistance) {
            answer++;
        }
    }
    
    return answer;
}
