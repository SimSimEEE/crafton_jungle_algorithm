function solution(numbers) {
    const answer = [];
    const stack = [];

    for (let i = 0; i < numbers.length; i++) {
        while (stack.length > 0 && numbers[i] > numbers[stack[stack.length - 1]]) {
            const index = stack.pop();
            answer[index] = numbers[i];
        }
        stack.push(i);
    }

    while (stack.length > 0) {
        const index = stack.pop();
        answer[index] = -1;
    }

    return answer;
}
