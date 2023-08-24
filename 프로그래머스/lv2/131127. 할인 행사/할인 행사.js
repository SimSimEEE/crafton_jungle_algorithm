function solution(want, number, discount) {
    var answer = 0;
    for(let i = 0; i <= discount.length - 10; i++){
        const discount_days = discount.slice(i, i + 10);
        let cnt = 0;
        for(let j = 0; j < want.length; j++){
            let fruit_num = discount_days.filter(element => want[j] === element).length;
            if(fruit_num <= number[j]){
                cnt += fruit_num;
            }
        }
        if(cnt === 10){
            answer++;
        }
    }
    return answer;
}