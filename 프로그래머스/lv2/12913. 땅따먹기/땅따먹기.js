function solution(land) {
    var answer = 0;
    land.unshift([0,0,0,0]);
    for(let i = 0; i < land.length - 1; i++){
        for(let j = 0; j < 4; j++){
            let maxNum = 0;
            for(let k = 0; k < 4; k++){
                if(k !== j){
                    maxNum = Math.max(maxNum, land[i][k]);
                }
            }
            land[i+1][j] += maxNum; 
        }
    }
    answer = Math.max.apply(null, land[land.length-1]);
    return answer;
}