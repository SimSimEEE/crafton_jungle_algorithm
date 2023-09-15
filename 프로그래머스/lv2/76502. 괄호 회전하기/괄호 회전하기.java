import java.util.*;
class Solution {
    public int solution(String s){
        int answer = 0;
        
        if(s.length()%2==1) return 0;
        
        else{
            for(int i = 0; i < s.length(); i++){
                answer += Check(s);
                s = s.substring(1, s.length()) + s.substring(0,1);
            }
        }
        return answer;
    }
    
    public int Check(String s){
        int answer = 1;
        Stack<Character> stack = new Stack<Character>();
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == '(' || c=='{' || c=='['){
                stack.push(c);
                continue;
            }
            else{
                if(!stack.isEmpty()){
                    char cnt_sign = stack.pop();
                    if(cnt_sign == '(' && c == ')') continue;
                    else if(c == cnt_sign+2) continue;
                }
            }
            answer--;
            break;
        }
        return answer;
    }
}