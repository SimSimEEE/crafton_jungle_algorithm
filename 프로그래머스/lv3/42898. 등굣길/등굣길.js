function solution(m, n, puddles) {
    const MOD = 1000000007;
    const graph = new Array(n).fill(null).map(() => new Array(m).fill(0));
    
    puddles.forEach(([x, y]) => {
        graph[y - 1][x - 1] = -1; 
    });
    
    graph[0][0] = 1;
    
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < m; j++) {
            if(graph[i][j] === -1) {
                graph[i][j] = 0;
                continue;
            }
            if(i > 0) {
                graph[i][j] += graph[i - 1][j]; 
            }
            if(j > 0) {
                graph[i][j] += graph[i][j - 1]; 
            }
            if(graph[i][j] >MOD)
                graph[i][j] %= MOD;
        }
    }
    
    return graph[n - 1][m - 1] % MOD; 
}
