function solution(s, skip, index) {
    var answer = '';
    const dictionary = [];
    for(let i = 0; i < 26; i++){
        const alpa = String.fromCharCode(i + 97);
        if(!skip.includes(alpa)){
            dictionary.push(alpa);
        }
    }
    [...s].forEach((c)=>{
        let i = (dictionary.indexOf(c) + index) % dictionary.length;
        answer += dictionary[i];
    });
    return answer;
}