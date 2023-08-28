function solution(s, skip, index) {
    var answer = '';
    const dictionary = [];
    let alphabet = [...'abcdefghijklmnopqrstuvwxyz'].filter(v => ![...skip].includes(v));
    [...s].forEach((c)=>{
        let i = (alphabet.indexOf(c) + index) % alphabet.length;
        answer += alphabet[i];
    });
    return answer;
}