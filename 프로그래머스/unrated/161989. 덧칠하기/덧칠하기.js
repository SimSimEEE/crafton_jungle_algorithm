function solution(n, m, section) {
    var answer = 0;
    let flag = 0;
    for(let i = 0; i < n; i++){
        let sec = section.shift(); 
        if(flag < sec){
            flag = sec + m - 1;
            answer++;
        }
    }
    return answer;
}