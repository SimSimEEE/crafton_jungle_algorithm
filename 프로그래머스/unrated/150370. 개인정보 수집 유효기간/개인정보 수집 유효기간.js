function days(year, month, day){
    return Number(year)*12*28 + Number(month)*28 + Number(day);
}

function solution(today, terms, privacies) {
    var answer = [];
    const termMap = [];
    terms.forEach((entry)=>{
        const arrayEntry = entry.split(" ");
        termMap[arrayEntry[0]] = Number(arrayEntry[1]);
    });
    const ArrayToday = today.split(".");
    const convertToday = days(ArrayToday[0], ArrayToday[1], ArrayToday[2]);
    privacies.forEach((entry, index)=>{
        const convertDay = entry.split(".");
        const tmp = convertDay.pop();
        convertDay.push(...tmp.split(" "));
        let contDay = days(convertDay[0], convertDay[1], convertDay[2]);
        contDay += termMap[convertDay[3]]*28;
        if(contDay <= convertToday){
            answer.push(index + 1);
        }
    });
    
    return answer;
}