function solution(participant, completion) {
    const hasharr = {};

    for (const person of participant) {
        hasharr[person] = (hasharr[person] || 0) + 1;
    }

    for (const person of completion) {
        hasharr[person] -= 1;
    }

    for (const person in hasharr) {
        if (hasharr[person] > 0) {
            return person;
        }
    }

    return null;
}
