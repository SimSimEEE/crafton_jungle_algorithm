function solution(k, score) {
    var answer = [];
    let queue = [];
    score.forEach((s, index)=>{
        if(queue.length < k){
            queue.push(s);
            answer.push(Math.min.apply(null, queue));
        }
        else{
            if(Math.min.apply(null, queue) < s){
                queue.splice(queue.indexOf(Math.min.apply(null, queue)),1);
                queue.push(s);
                answer.push(Math.min.apply(null, queue));
            }
            else{
                answer.push(Math.min.apply(null, queue));
            }
        }
    });
    return answer;
}