function solution(arr)
{
    answer = [];
    arr.forEach((a)=>{
        const tmp = answer.pop();
        if(tmp !== a)
            answer.push(tmp);
        answer.push(a);
    });
    answer.shift();
    return answer;
}