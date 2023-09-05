function solution(sequence, k) {
    const answer = [0, sequence.length - 1];
    let i = 0;
    let j = 0;
    let sumNum = 0;

    while (j < sequence.length) {
        sumNum += sequence[j];

        while (sumNum > k) {
            sumNum -= sequence[i];
            i++;
        }

        if (sumNum === k) {
            if(answer[1] - answer[0] > j - i){
                answer[0] = i;
                answer[1] = j
            }
        }

        j++;
    }

    return answer;
}
