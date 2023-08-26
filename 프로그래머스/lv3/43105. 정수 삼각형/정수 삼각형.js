function solution(triangle) {
    const numRows = triangle.length;

    for (let row = 1; row < numRows; row++) {
        for (let col = 0; col <= row; col++) {
            if (col === 0) {
                triangle[row][col] += triangle[row - 1][col];
            } else if (col === row) {
                triangle[row][col] += triangle[row - 1][col - 1];
            } else {
                triangle[row][col] += Math.max(triangle[row - 1][col - 1], triangle[row - 1][col]);
            }
        }
    }

    return Math.max(...triangle[numRows - 1]);
}
