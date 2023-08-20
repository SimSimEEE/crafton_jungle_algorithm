function solution(n, works) {
    var answer = 0;
    works.sort(function(a,b){
        return b-a;
    });
    for(let i = 0; i < n; i++){
        for(let j = 1; j <= works.length; j++)
            if(works[0] < works[j]){
                [works[0], works[j]] = [works[j], works[0]];
                break;
            }
        if(works[0]!==0)
            works[0]--;
    }
    works.forEach((w)=>{
       answer += w**2; 
    });
    console.log(works);
    return answer;
}