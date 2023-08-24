function solution(participant, completion) {
    var answer = '';
    let hashmap = [];
    participant.forEach(entry=>{
        hashmap[entry] = hashmap[entry]? hashmap[entry] + 1: 1;
    });
    completion.forEach(entry=>{
        hashmap[entry]--;
    });
    for(const key in hashmap){
        if(hashmap[key] === 1){
            answer = key;
            break;
        }
    }
    return answer;
}