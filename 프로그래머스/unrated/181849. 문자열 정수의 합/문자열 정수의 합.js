function solution(num_str) {
    var answer = 0;
    [...num_str].forEach((n)=>{
        answer += parseInt(n);
    });
    return answer;
}