function solution(k, dungeons) {
    var answer = -1;
    let maxAdventure = dungeons.length;
    const arr = getPermutations(dungeons, maxAdventure);
    let maxNum = 0;
    arr.forEach((entry)=>{
        let tmpNum = 0;
        let tmpK = k;
        for(e of entry){
            if(e[0] <= tmpK){
                tmpK-=e[1];
                tmpNum++;
            }
            else{
                maxNum = Math.max(maxNum,tmpNum);
                break;
            }
        }
        maxNum = Math.max(maxNum,tmpNum);
    });
    return maxNum;
}

 const getPermutations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]); 
    arr.forEach((fixed, index, origin) => {
      const rest = [...origin.slice(0, index), ...origin.slice(index+1)] 
      const permutations = getPermutations(rest, selectNumber - 1); 
      const attached = permutations.map((el) => [fixed, ...el]); 
      results.push(...attached); 
    });

    return results;
}