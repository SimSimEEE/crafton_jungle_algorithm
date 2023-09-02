function solution(arr) {
    var answer = [];
    arr.forEach((entry)=>{
        for(let i = 0; i < entry; i++){
            answer.push(entry);
        }
    })
    return answer;
}