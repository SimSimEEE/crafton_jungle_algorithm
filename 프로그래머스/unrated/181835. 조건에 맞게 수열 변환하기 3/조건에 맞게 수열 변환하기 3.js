function solution(arr, k) {
    var answer = [];
    if(k % 2 === 0){
        answer = arr.map(function(e){
            return e + k;
        });
    }
    else{
        answer = arr.map(function(e){
            return e * k;
        });
    }
    return answer;
}