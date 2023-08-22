function solution(numbers, target) {
    var answer = 0;
    array = [];
    const n = 2**numbers.length;
    for(let i = 0; i < n; i++){
        array[i] = 0;
        for(let j = 0; j < numbers.length; j++){
            array[i] += (Math.floor(i/(2**(numbers.length -j - 1)))%2 === 0?1:-1)*numbers[j];
        }
    }
    array.forEach((a)=>{
        if(a === target)
            answer++;
    });
    return answer;
}