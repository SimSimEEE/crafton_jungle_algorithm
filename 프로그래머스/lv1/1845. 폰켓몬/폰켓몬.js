function solution(nums) {
    var answer = 0;
    const collectNum = nums.length/2;
    const setNum = new Set(nums);
    return setNum.size < collectNum? setNum.size:collectNum;
}