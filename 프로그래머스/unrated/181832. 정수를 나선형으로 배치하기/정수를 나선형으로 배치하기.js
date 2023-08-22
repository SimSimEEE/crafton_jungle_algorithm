function solution(n) {
    var answer = Array.from(Array(n), ()=> Array(n).fill(0));
    let i = 0;
    let j = 0;
    let start = 2;
    answer[0][0] = 1
    while(!answer.includes(0) && start < n*n){
        while(j < n && answer[i][j+1] === 0){
            answer[i][++j] = start++;
        }
        while(i < n-1 && answer[i+1][j] === 0){
            answer[++i][j] = start++;
        }
        while(j > 0 && answer[i][j-1] === 0){
            answer[i][--j] = start++;
        }
        while(i > 0 && answer[i-1][j] === 0){
            answer[--i][j] = start++;
        }
    }
    if(n%2 ===1){
        answer[Math.floor(n/2)][Math.floor(n/2)] = n*n;
    }
    return answer;
}