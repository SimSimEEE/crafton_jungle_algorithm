function solution(r1, r2) {
    var answer = 0;
    for(let i = 1; i <= r2; i++){
        let maxnum = Math.floor(Math.sqrt(r2*r2 - i*i))
        let minnum = Math.ceil(Math.sqrt(r1*r1 - i*i))
        if(!minnum)
            minnum = 0;
        answer += maxnum - minnum +1;
    }
    return answer * 4;
}