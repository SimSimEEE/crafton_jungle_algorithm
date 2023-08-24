function solution(arr, k) {
    var answer = [];
    answer = arr.map(function(e){
        return k%2 === 1? e*k:e+k;
    });
    return answer;
}