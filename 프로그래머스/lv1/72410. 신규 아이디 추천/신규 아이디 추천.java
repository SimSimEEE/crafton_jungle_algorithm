import java.util.*;
class Solution {
    public String solution(String new_id) {
        String answer = "";
        answer = new_id.toLowerCase();
        answer = answer.replaceAll("[^-_.0-9a-z]","");
        answer = answer.replaceAll("[..]{2,}",".");
        answer = answer.replaceAll("^[.]|[.]$","");
        answer = answer.equals("") ? "a" :answer;
        if(answer.length()>=16){
            answer = answer.substring(0,15);
            answer = answer.replaceAll("[.]$","");
        }
        if(answer.length() < 3){
            for(int i = 0; i <= 3 - answer.length(); i++)
                answer += answer.charAt(answer.length()-1);
        }
        return answer;
    }
}