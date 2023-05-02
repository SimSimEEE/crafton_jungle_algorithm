class Solution {
    public int solution(int[][] triangle) {
        int ln = triangle.length;
        for(int i = 1; i < ln; i++){
            int tri_ln = triangle[i].length-1;
            triangle[i][0] += triangle[i-1][0];
            triangle[i][tri_ln] += triangle[i-1][tri_ln-1];
            for(int j = 1; j < i; j++){
                if(triangle[i-1][j] > triangle[i-1][j-1])
                    triangle[i][j] += triangle[i-1][j];
                else
                    triangle[i][j] += triangle[i-1][j-1];
            }
        }
        int answer = triangle[ln-1][0];
        for(int i=0; i<ln; i++) {
            if(answer<triangle[ln-1][i]) {
                answer = triangle[ln-1][i];
            }
        }
        return answer;
    }
}