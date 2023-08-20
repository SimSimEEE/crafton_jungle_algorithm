function solution(wallpaper) {
    var answer = [50, 50, 0, 0];
    wallpaper.forEach((W, index)=>{
        for(i in W){
            if(W[i] === '#'){
                answer[0] = Math.min(answer[0], index);
                answer[1] = Math.min(answer[1], parseInt(i));
                answer[2] = Math.max(answer[2], index + 1);
                answer[3] = Math.max(answer[3], parseInt(i) + 1);
            }
        }
    });
    return answer;
}