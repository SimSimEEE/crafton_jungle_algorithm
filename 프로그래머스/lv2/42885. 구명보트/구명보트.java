import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int i = people.length-1; int j = 0;
        Arrays.sort(people);
        for(; i > j; i--){
            if(people[i] + people[j] <= limit){
                j++;
            }
        }
        return people.length - j;
    }
}