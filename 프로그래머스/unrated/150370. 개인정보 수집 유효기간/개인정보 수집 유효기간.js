function days(year, month, day) {
    return Number(year) * 12 * 28 + Number(month) * 28 + Number(day);
}

function extractDayInfo(dayString) {
    const parts = dayString.split(".");
    const day = parts.pop();
    parts.push(...day.split(" "));
    return {
        year: parts[0],
        month: parts[1],
        day: parts[2],
        term: parts[3]
    };
}

function solution(today, terms, privacies) {
    const termMap = {};
    terms.forEach((entry) => {
        const [term, value] = entry.split(" ");
        termMap[term] = Number(value);
    });

    const convertedToday = days(...today.split("."));
    const answer = [];

    privacies.forEach((entry, index) => {
        const { year, month, day, term } = extractDayInfo(entry);
        let dayValue = days(year, month, day) + termMap[term] * 28;
        
        if (dayValue <= convertedToday) {
            answer.push(index + 1);
        }
    });

    return answer;
}
