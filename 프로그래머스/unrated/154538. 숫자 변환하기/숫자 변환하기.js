function solution(x, y, n) {
    const arr = new Array(y + 1).fill(Infinity); 
    arr[x] = 0; 

    for (let i = x; i <= y; i++) {
        if (arr[i] === Infinity) continue; 

        const nextPositions = [i + n, i * 2, i * 3];
        for (const nextPos of nextPositions) {
            if (nextPos <= y) {
                arr[nextPos] = Math.min(arr[nextPos], arr[i] + 1);
            }
        }
    }

    return arr[y] === Infinity ? -1 : arr[y];
}
