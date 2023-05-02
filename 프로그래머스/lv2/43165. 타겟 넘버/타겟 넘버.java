class Solution {
    public int solution(int[] numbers, int target) {
        int num_ln = numbers.length;
        int result_ln = (int)Math.pow(2,num_ln);
        int[] result = new int[result_ln];
        int answer = 0;
        for(int i = 0; i < result_ln; i++){
            for(int j = 0; j < num_ln; j++){
                result[i] += (int) Math.pow(-1,i/(result_ln/(int)Math.pow(2,j+1)))*numbers[j];
            }
            if(result[i] == target) answer++;
        }
        return answer;
    }
}