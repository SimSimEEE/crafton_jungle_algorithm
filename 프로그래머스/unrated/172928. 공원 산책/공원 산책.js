function solution(park, routes) {
    let answer = [];

    for (let rowIndex = 0; rowIndex < park.length; rowIndex++) {
        const colIndex = park[rowIndex].indexOf('S');
        if (colIndex !== -1) {
            answer = [rowIndex, colIndex];
            break;
        }
    }

    routes.forEach(entry => {
        const move = entry.split(' ');
        let tmpRow = answer[0];
        let tmpCol = answer[1];
        let flag = true;

        for (let i = 0; i < Number(move[1]); i++) {
            if (move[0] === 'N') tmpRow--;
            else if (move[0] === 'S') tmpRow++;
            else if (move[0] === 'W') tmpCol--;
            else tmpCol++;

            if (
                tmpRow < 0 || tmpRow >= park.length ||
                tmpCol < 0 || tmpCol >= park[0].length ||
                park[tmpRow][tmpCol] === 'X'
            ) {
                flag = false;
                break;
            }
        }

        if (flag) {
            answer = [tmpRow, tmpCol];
        }
    });

    return answer;
}
