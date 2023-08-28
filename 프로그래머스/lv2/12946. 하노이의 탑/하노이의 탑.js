function solution(n) {
    const answer = [];
    function hanoi(num, from, to, through){
    if(num == 0)
        return;
    hanoi(num-1, from, through, to);
    answer.push([from, to]);
    hanoi(num-1, through, to, from);
    }
    hanoi(n, 1, 3, 2);
    return answer;
}