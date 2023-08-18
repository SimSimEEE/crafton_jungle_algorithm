function solution(keymap, targets) {
    var answer = [];
    targets.forEach((target, index)=>{
        answer[index] = 0;
        for(i in target){
            min_key = [];
            keymap.forEach((key)=>{
                if(key.indexOf(target[i])!==-1)
                    min_key.push(key.indexOf(target[i]) + 1);
            })
            if(min_key){
                answer[index] += Math.min.apply(null, min_key);
            }
        }
        if(answer[index] === Infinity)
            answer[index] = -1;
    });
    return answer;
}