function solution(nums) {
    const setNum = new Set(nums);
    return setNum.size < nums.length/2? setNum.size : nums.length/2;
}