function solution(m, n, board) {
    let graph = Array.from({ length: n }, () => []);
    board.forEach((line, i) => {
        for (let j = 0; j < n; j++) {
            graph[j].push(line[j]);
        }
    });

    const dx = [1, 0, 1];
    const dy = [0, 1, 1];

    while (true) {
        let isChanged = false;
        const explodes = [];

        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < m - 1; j++) {
                if (graph[i][j] === "-") continue;

                const [x, y] = [i, j];
                const blocks = [];

                for (let k = 0; k < 3; k++) {
                    const nx = x + dx[k];
                    const ny = y + dy[k];

                    if (nx < n && ny < m) {
                        if (graph[x][y] === graph[nx][ny]) {
                            blocks.push([nx, ny]);
                        } else {
                            break;
                        }
                    } else {
                        break;
                    }
                }

                if (blocks.length === 3) {
                    explodes.push([x, y]);
                    explodes.push(...blocks);
                }
            }
        }

        if (explodes.length === 0) {
            break; 
        }

        explodes.forEach(([x, y]) => {
            graph[x][y] = "-";
        });

        isChanged = true;

        for (let i = 0; i < n; i++) {
            graph[i] = graph[i].filter(block => block !== "-");
            while (graph[i].length < m) {
                graph[i].unshift("-");
            }
        }

        if (!isChanged) {
            break;
        }
    }

    return graph.flat().filter(block => block === "-").length;
}
