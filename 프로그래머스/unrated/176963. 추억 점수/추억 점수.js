function solution(name, yearning, photo) {
    var answer = [];
    let nameAndYearning = {};
    name.forEach((name, index)=>{
        nameAndYearning[name] = yearning[index]
    });
    photo.forEach((array, index)=>{
        let tmp = 0;
        array.forEach((people)=>{
           tmp += (nameAndYearning[people] || 0); 
        });
        answer.push(tmp);
    });
    return answer;
}