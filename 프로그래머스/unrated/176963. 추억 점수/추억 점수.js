function solution(name, yearning, photo) {
    var answer = [];
    let nameAndYearning = {};
    name.forEach((name, index)=>{
        nameAndYearning[name] = yearning[index]
    });
    photo.forEach((array, index)=>{
        if(!answer[index]){
            answer[index] = 0;
        }
        array.forEach((people)=>{
           answer[index] += (nameAndYearning[people] || 0); 
        });
    });
    return answer;
}