function solution(elements) {
    const numSet = new Set();
    const totalElements = elements.length;

    for (let windowSize = 1; windowSize <= totalElements; windowSize++) {
        let sumNum = 0;

        for (let index = 0; index < totalElements + windowSize; index++) {
            if (index < windowSize) {
                sumNum += elements[index];
            } else {
                numSet.add(sumNum);

                if (index < totalElements) {
                    sumNum += elements[index];
                    sumNum -= elements[index - windowSize];
                } else {
                    sumNum += elements[index - totalElements];
                    sumNum -= elements[index - windowSize];
                }
            }
        }
    }

    return numSet.size;
}