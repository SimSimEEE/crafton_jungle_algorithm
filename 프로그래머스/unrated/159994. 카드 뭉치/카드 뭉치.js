function solution(cards1, cards2, goal) {
    for(i in goal){
        if(cards1[0] === goal[i]){
            cards1.shift();
        }
        else if(cards2[0] === goal[i]){
            cards2.shift();
        }
        else{
            return "No";
        }
    }
    return "Yes";
}