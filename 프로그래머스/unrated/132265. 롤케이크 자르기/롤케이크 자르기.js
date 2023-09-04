function solution(toppings) {
    const toppingCountA = Array(10001).fill(0);
    const toppingCountB = Array(10001).fill(0);
    let answer = 0;
    let distinctToppingsA = 0;
    let distinctToppingsB = 0;

    function processTopping(topping) {
        if (toppingCountA[topping] === 0) distinctToppingsA++;
        toppingCountA[topping]++;
        toppingCountB[topping]--;
        if (toppingCountB[topping] === 0) distinctToppingsB--;
        if (distinctToppingsA === distinctToppingsB) answer++;
    }

    for (const topping of toppings) {
        toppingCountB[topping]++;
    }
    distinctToppingsB = toppingCountB.filter(count => count !== 0).length;

    for (const topping of toppings) {
        processTopping(topping);
    }

    return answer;
}
