function solution(s) {
    var answer = [];
    for(i in s){
        answer[i] = -1;
        for(let j = i-1; j >=0; j--){
            if(s[i] === s[j]){
                answer[i] = i - j;
                break;
            }
        }
    }
    return answer;
}