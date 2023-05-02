class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {2,2};
        while(yellow != (answer[0]-2)*(answer[1]-2) || brown/2 != answer[0]+answer[1]-2){
            answer[0] = brown/2 -(++answer[1])+2;
        }
        return answer;
    }
}