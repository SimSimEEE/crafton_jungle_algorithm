class Solution {
    public String solution(int n) {
        String ans = "";
        while(n!=0) {
            --n;
            if(n%3 == 0) ans = 1 + ans;
            else if(n%3 == 1) ans = 2 + ans;
            else if(n%3 == 2) ans = 4 + ans;
            n /= 3;
        }        
        return ans;
    }
}