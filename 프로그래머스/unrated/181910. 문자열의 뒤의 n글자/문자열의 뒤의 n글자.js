function solution(my_string, n) {
    var answer = my_string.substr(my_string.length - n,n);
    return answer;
}